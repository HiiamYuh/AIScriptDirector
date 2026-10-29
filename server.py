import os
import sys
import json
import uuid
import shutil
import asyncio
from typing import Optional
from pathlib import Path

# Ensure UTF-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from config import BASE_DIR, OUTPUTS_DIR, save_config
from ai_engine import ScriptGenerator

app = FastAPI(title="AI YouTube Script Director", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(exist_ok=True)
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>Tool Kịch Bản AI YouTube đang khởi động...</h1>")

@app.get("/api/config")
async def get_config():
    openai_key = os.getenv("OPENAI_API_KEY", "")
    gemini_key = os.getenv("GEMINI_API_KEY", "")
    provider = os.getenv("DEFAULT_PROVIDER", "openai")
    
    return {
        "provider": provider,
        "has_openai": bool(openai_key),
        "openai_masked": f"{openai_key[:7]}...{openai_key[-4:]}" if len(openai_key) > 12 else ("Có key" if openai_key else "Chưa có"),
        "has_gemini": bool(gemini_key),
        "gemini_masked": f"{gemini_key[:7]}...{gemini_key[-4:]}" if len(gemini_key) > 12 else ("Có key" if gemini_key else "Chưa có"),
    }

@app.post("/api/config")
async def update_config(data: dict):
    openai_key = data.get("openai_key")
    gemini_key = data.get("gemini_key")
    provider = data.get("provider")
    save_config(openai_key=openai_key, gemini_key=gemini_key, provider=provider)
    return {"status": "success", "message": "Đã lưu cấu hình API thành công!"}

@app.post("/api/test-key")
async def test_key(data: dict):
    provider = data.get("provider", "gemini")
    key = data.get("key")
    if not key:
        if provider == "gemini":
            key = os.getenv("GEMINI_API_KEY", "")
        else:
            key = os.getenv("OPENAI_API_KEY", "")

    if not key:
        return {"status": "error", "message": "Chưa có API Key để kiểm tra!"}

    try:
        gen = ScriptGenerator(provider=provider, api_key=key)
        reply = gen._call_ai("Xin chào, hãy trả lời đúng 2 từ: Sẵn sàng.")
        return {"status": "success", "message": f"Kết nối AI thành công! Phản hồi: {reply.strip()}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/generate-outline-stream")
async def generate_outline_stream(
    topic: str = Form(...),
    video_type: str = Form("Video dài (16:9)"),
    genre: str = Form("Bí ẩn / Ly kỳ"),
    total_scenes: int = Form(55),
    provider: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    """Streaming endpoint for Step 1: generates outline only (~5-10s)."""
    image_path = None
    if image and image.filename:
        filename = f"{uuid.uuid4().hex}_{image.filename}"
        dest_path = UPLOAD_DIR / filename
        with open(dest_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_path = str(dest_path)

    async def event_generator():
        queue = asyncio.Queue()
        loop = asyncio.get_event_loop()

        def sync_progress(percent: int, message: str):
            asyncio.run_coroutine_threadsafe(
                queue.put({"type": "progress", "percent": percent, "message": message}),
                loop
            )

        def worker():
            try:
                gen = ScriptGenerator(provider=provider, api_key=api_key)
                part1_text = gen.generate_outline(
                    topic=topic,
                    image_path=image_path,
                    video_type=video_type,
                    genre=genre,
                    total_scenes=total_scenes,
                    progress_callback=sync_progress
                )
                
                script_id = uuid.uuid4().hex[:8]
                result = {
                    "id": script_id,
                    "topic": topic,
                    "video_type": video_type,
                    "genre": genre,
                    "total_scenes": total_scenes,
                    "part1_outline": part1_text,
                    "full_markdown": part1_text,
                    "scenes": []
                }
                
                # Save draft
                out_file = OUTPUTS_DIR / f"script_{script_id}.json"
                with open(out_file, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)

                md_file = OUTPUTS_DIR / f"script_{script_id}.md"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(part1_text)

                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "complete", "data": result}),
                    loop
                )
            except Exception as e:
                import traceback
                traceback.print_exc()
                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "error", "message": str(e)}),
                    loop
                )
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(None), loop)

        loop.run_in_executor(None, worker)

        while True:
            item = await queue.get()
            if item is None:
                break
            payload = json.dumps(item, ensure_ascii=False)
            yield f"data: {payload}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

@app.post("/api/generate-scenes-stream")
async def generate_scenes_stream(
    topic: str = Form(...),
    part1_outline: str = Form(...),
    script_id: Optional[str] = Form(None),
    video_type: str = Form("Video dài (16:9)"),
    genre: str = Form("Bí ẩn / Ly kỳ"),
    total_scenes: int = Form(55),
    provider: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None)
):
    """Streaming endpoint for Step 2: generates detailed scene breakdown from outline."""
    async def event_generator():
        queue = asyncio.Queue()
        loop = asyncio.get_event_loop()

        def sync_progress(percent: int, message: str):
            asyncio.run_coroutine_threadsafe(
                queue.put({"type": "progress", "percent": percent, "message": message}),
                loop
            )

        def worker():
            try:
                gen = ScriptGenerator(provider=provider, api_key=api_key)
                result = gen.generate_scenes_from_outline(
                    topic=topic,
                    part1_outline=part1_outline,
                    video_type=video_type,
                    genre=genre,
                    total_scenes=total_scenes,
                    progress_callback=sync_progress
                )

                sid = script_id or uuid.uuid4().hex[:8]
                result["id"] = sid

                # Save output to outputs folder
                out_file = OUTPUTS_DIR / f"script_{sid}.json"
                with open(out_file, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)

                md_file = OUTPUTS_DIR / f"script_{sid}.md"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(result["full_markdown"])

                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "complete", "data": result}),
                    loop
                )
            except Exception as e:
                import traceback
                traceback.print_exc()
                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "error", "message": str(e)}),
                    loop
                )
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(None), loop)

        loop.run_in_executor(None, worker)

        while True:
            item = await queue.get()
            if item is None:
                break
            payload = json.dumps(item, ensure_ascii=False)
            yield f"data: {payload}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

@app.post("/api/generate-stream")
async def generate_stream(
    topic: str = Form(...),
    video_type: str = Form("Video dài (16:9)"),
    genre: str = Form("Bí ẩn / Ly kỳ"),
    total_scenes: int = Form(55),
    provider: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    """Streaming endpoint that yields progress updates and the final script."""
    # Handle image upload if provided
    image_path = None
    if image and image.filename:
        filename = f"{uuid.uuid4().hex}_{image.filename}"
        dest_path = UPLOAD_DIR / filename
        with open(dest_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_path = str(dest_path)

    async def event_generator():
        queue = asyncio.Queue()
        loop = asyncio.get_event_loop()

        def sync_progress(percent: int, message: str):
            asyncio.run_coroutine_threadsafe(
                queue.put({"type": "progress", "percent": percent, "message": message}),
                loop
            )

        def worker():
            try:
                gen = ScriptGenerator(provider=provider, api_key=api_key)
                result = gen.generate_full_script_pipeline(
                    topic=topic,
                    image_path=image_path,
                    video_type=video_type,
                    genre=genre,
                    total_scenes=total_scenes,
                    progress_callback=sync_progress
                )
                
                # Save output to outputs folder
                script_id = uuid.uuid4().hex[:8]
                out_file = OUTPUTS_DIR / f"script_{script_id}.json"
                result["id"] = script_id
                with open(out_file, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)

                # Save markdown file as well
                md_file = OUTPUTS_DIR / f"script_{script_id}.md"
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(result["full_markdown"])
                    
                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "complete", "data": result}),
                    loop
                )
            except Exception as e:
                import traceback
                traceback.print_exc()
                asyncio.run_coroutine_threadsafe(
                    queue.put({"type": "error", "message": str(e)}),
                    loop
                )
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(None), loop)

        # Run worker in background thread
        loop.run_in_executor(None, worker)

        while True:
            item = await queue.get()
            if item is None:
                break
            payload = json.dumps(item, ensure_ascii=False)
            yield f"data: {payload}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )

@app.post("/api/parse-and-save")
async def parse_and_save(data: dict):
    """Allows importing a script generated by Gemini Argon directly without an API key."""
    raw_text = data.get("text", "")
    topic = data.get("topic", "Kịch bản tạo bởi Gemini Argon")
    video_type = data.get("video_type", "Video dài (16:9)")
    genre = data.get("genre", "Tùy chỉnh")

    if not raw_text.strip():
        raise HTTPException(status_code=400, detail="Vui lòng nhập nội dung kịch bản!")

    gen = ScriptGenerator()
    parsed_scenes = gen.parse_scenes_from_text(raw_text)

    # Extract part 1 if present
    part1 = raw_text
    if "PHẦN 2:" in raw_text:
        part1 = raw_text.split("PHẦN 2:")[0].strip()
    elif "### [CẢNH 01]" in raw_text:
        part1 = raw_text.split("### [CẢNH 01]")[0].strip()

    script_id = uuid.uuid4().hex[:8]
    result = {
        "id": script_id,
        "topic": topic,
        "video_type": video_type,
        "genre": genre,
        "total_scenes": len(parsed_scenes),
        "part1_outline": part1,
        "full_markdown": raw_text,
        "scenes": parsed_scenes
    }

    out_file = OUTPUTS_DIR / f"script_{script_id}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    md_file = OUTPUTS_DIR / f"script_{script_id}.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(raw_text)

    return result

@app.get("/api/history")
async def get_history():
    history = []
    for file in sorted(OUTPUTS_DIR.glob("script_*.json"), key=os.path.getmtime, reverse=True):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                history.append({
                    "id": data.get("id", file.stem.replace("script_", "")),
                    "topic": data.get("topic", "Không có tiêu đề"),
                    "scenes_count": data.get("total_scenes", len(data.get("scenes", []))),
                    "video_type": data.get("video_type", ""),
                    "genre": data.get("genre", ""),
                    "filename": file.name
                })
        except Exception:
            continue
    return history

@app.get("/api/history/{script_id}")
async def get_history_detail(script_id: str):
    json_path = OUTPUTS_DIR / f"script_{script_id}.json"
    if not json_path.exists():
        raise HTTPException(status_code=404, detail="Không tìm thấy kịch bản")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/api/export-csv")
async def export_csv(data: dict):
    scenes = data.get("scenes", [])
    csv_lines = [
        "Cảnh,Thời lượng,Góc máy,Prompt Midjourney / Flux (Ảnh),Prompt Video (Kling/Runway),Voice-Over (Lời bình),Sound FX & Âm thanh"
    ]
    for s in scenes:
        c_num = s.get("scene_number", "")
        c_timing = f'"{s.get("timing", "")}"'
        c_camera = f'"{s.get("camera", "")}"'
        c_img = f'"{s.get("image_prompt", "").replace(chr(34), chr(34)+chr(34))}"'
        c_vid = f'"{s.get("video_prompt", "").replace(chr(34), chr(34)+chr(34))}"'
        c_vo = f'"{s.get("voiceover", "").replace(chr(34), chr(34)+chr(34))}"'
        c_sfx = f'"{s.get("sound_fx", "").replace(chr(34), chr(34)+chr(34))}"'
        csv_lines.append(f"{c_num},{c_timing},{c_camera},{c_img},{c_vid},{c_vo},{c_sfx}")

    # Add UTF-8 BOM so Excel opens Vietnamese characters correctly
    csv_content = "\ufeff" + "\n".join(csv_lines)
    return StreamingResponse(
        iter([csv_content]),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=kich_ban_ai_scenes.csv"}
    )

if __name__ == "__main__":
    import webbrowser
    port = 8000
    print(f"Starting Tool Kịch Bản AI YouTube at http://127.0.0.1:{port}")
    webbrowser.open(f"http://127.0.0.1:{port}")
    uvicorn.run("server:app", host="127.0.0.1", port=port, reload=False)
