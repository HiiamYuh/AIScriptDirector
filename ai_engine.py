import os
import re
import json
import base64
from typing import Generator, Dict, Any, List, Optional
from pathlib import Path
from PIL import Image

import openai
from google import genai
from google.genai import types

from config import DEFAULT_OPENAI_KEY, DEFAULT_GEMINI_KEY, DEFAULT_GROQ_KEY, DEFAULT_PROVIDER

SYSTEM_INSTRUCTION = """Bạn là một ĐẠO DIỄN NỘI DUNG VÀ CHUYÊN GIA KỊCH BẢN VIDEO AI YOUTUBE ĐẲNG CẤP QUỐC TẾ (Senior YouTube AI Video Producer & Prompt Engineer).
Nhiệm vụ của bạn là: Phân tích kỹ lưỡng bức ảnh người dùng cung cấp (nhân vật, bối cảnh, ánh sáng, cảm xúc, phong cách mỹ thuật) và sáng tác một kịch bản video AI YouTube đỉnh cao, sẵn sàng đưa vào sản xuất ngay lập tức với các công cụ: Midjourney, Flux, Kling AI, Runway Gen-3, Luma Dream Machine, ElevenLabs, CapCut.

BẮT BUỘC TUÂN THỦ CÁC NGUYÊN TẮC GIỮ CHÂN NGƯỜI XEM (RETENTION & VIRALITY):
1. THE 3-SECOND HOOK (Mở đầu 3 giây đầu tiên):
   - Phải có cú sốc thị giác (Visual Hook), cú sốc âm thanh (Audio Pattern Interrupt), và câu nói kích thích trí tò mò cực độ (Curiosity Gap).
   - TUYỆT ĐỐI KHÔNG bắt đầu bằng: "Chào mừng các bạn", "Hôm nay chúng ta sẽ tìm hiểu...". Phải đi thẳng vào tình huống nghẹt thở hoặc câu hỏi bí ẩn.
2. NHỊP ĐỘ DỰNG PHIM (PACING):
   - Mỗi cảnh chỉ nên kéo dài từ 3 đến 6 giây (đối với Shorts) hoặc 4 đến 7 giây (đối với Video dài) để kích thích thị giác liên tục.
   - Luân chuyển góc máy: Toàn cảnh (Wide Shot) -> Cận cảnh (Close-up) -> Góc quay kịch tính (Low angle / Over the shoulder).
3. PROMPT TẠO ẢNH CHUYÊN NGHIỆP (Midjourney v6 / Flux.1):
   - Viết bằng tiếng Anh chuẩn Prompt Engineering.
   - Đầy đủ: Subject + Action + Camera Angle/Lens + Lighting (volumetric, cinematic, rim light) + Style/Art aesthetic + Aspect Ratio tag (--ar 9:16 cho Shorts hoặc --ar 16:9 cho Video dài).
   - Duy trì ngoại hình nhân vật nhất quán qua các cảnh.
4. PROMPT TẠO CHUYỂN ĐỘNG VIDEO (Kling AI / Runway Gen-3 / Luma / Hailuo):
   - Hướng dẫn chuyển động camera rõ ràng: [Slow cinematic push in], [Dynamic camera pan left], [Subtle handheld shake], [Slow-motion hair flow, particle floating].
5. VOICE-OVER (LỜI BÌNH):
   - Ngắn gọn, súc tích, văn phong tự nhiên, giàu cảm xúc, có chỉ dẫn ngữ điệu [thì thầm], [dồn dập], [ngắt nghỉ 1s].
6. YOUTUBE VIRAL PACKAGING:
   - 5 tiêu đề kích thích CTR cao (không lừa dối nhưng khơi gợi tò mò).
   - 3 ý tưởng Thumbnail với Text Overlay tối đa 3-4 từ cực kỳ kích thích tò mò.
   - Mô tả video chuẩn SEO kèm mốc Timeline và Hashtags.

YÊU CẦU CẤU TRÚC KỊCH BẢN CHÍNH XÁC:
Kịch bản gồm 2 phần duy nhất:
PHẦN 1: KỊCH BẢN SƯỜN & TÓM TẮT NỘI DUNG CHÍNH (Outline, Cốt truyện, Khóa nhân vật & mỹ thuật, The 3-Second Hook, 5 Tiêu đề giật gân, 3 Thumbnail, Mô tả SEO).
PHẦN 2: CHI TIẾT KỊCH BẢN KHOẢNG 50-60 PROMPT (Chi tiết từ Cảnh 1 đến cảnh cuối cùng, mỗi cảnh có đầy đủ Prompt Ảnh, Prompt Video, Voice-Over, Sound FX).
"""

def encode_image_to_base64(image_path: str) -> tuple[str, str]:
    """Return (base64_string, mime_type)"""
    ext = Path(image_path).suffix.lower()
    mime = "image/jpeg"
    if ext in [".png"]:
        mime = "image/png"
    elif ext in [".webp"]:
        mime = "image/webp"
    elif ext in [".gif"]:
        mime = "image/gif"
        
    with open(image_path, "rb") as image_file:
        b64 = base64.b64encode(image_file.read()).decode('utf-8')
    return b64, mime

class ScriptGenerator:
    def __init__(self, provider: str = None, api_key: str = None):
        self.provider = provider or os.getenv("DEFAULT_PROVIDER", "gemini")
        self.openai_key = api_key if (api_key and self.provider == "openai") else (os.getenv("OPENAI_API_KEY", "") or DEFAULT_OPENAI_KEY)
        self.gemini_key = api_key if (api_key and self.provider == "gemini") else (os.getenv("GEMINI_API_KEY", "") or DEFAULT_GEMINI_KEY)
        self.groq_key = api_key if (api_key and self.provider == "groq") else (os.getenv("GROQ_API_KEY", "") or DEFAULT_GROQ_KEY)
        
    def _call_openai(self, prompt: str, image_path: Optional[str] = None, system_prompt: str = SYSTEM_INSTRUCTION) -> str:
        try:
            client = openai.OpenAI(api_key=self.openai_key)
            messages = [{"role": "system", "content": system_prompt}]
            
            user_content = []
            if image_path and os.path.exists(image_path):
                b64, mime = encode_image_to_base64(image_path)
                user_content.append({
                    "type": "image_url",
                    "image_url": {"url": f"data:{mime};base64,{b64}"}
                })
            
            user_content.append({"type": "text", "text": prompt})
            messages.append({"role": "user", "content": user_content})
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.7,
                max_tokens=8192
            )
            return response.choices[0].message.content or ""
        except openai.RateLimitError as e:
            raise ValueError("Tài khoản OpenAI đã hết hạn mức (Quota Exceeded). Vui lòng chuyển sang dùng Google Gemini (hoàn toàn miễn phí tại https://aistudio.google.com/) hoặc nạp thêm quota OpenAI!")
        except Exception as e:
            raise ValueError(f"Lỗi gọi OpenAI: {str(e)}")

    def _call_groq(self, prompt: str, system_prompt: str = SYSTEM_INSTRUCTION) -> str:
        try:
            client = openai.OpenAI(api_key=self.groq_key, base_url="https://api.groq.com/openai/v1")
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                max_tokens=8000
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            raise ValueError(f"Lỗi gọi Groq: {str(e)}")

    def _call_gemini(self, prompt: str, image_path: Optional[str] = None, system_prompt: str = SYSTEM_INSTRUCTION) -> str:
        if not self.gemini_key:
            raise ValueError("Chưa thiết lập GEMINI_API_KEY! Hãy nhập key tại giao diện hoặc dán vào file .env.")
        try:
            client = genai.Client(api_key=self.gemini_key)
            contents = []
            if image_path and os.path.exists(image_path):
                try:
                    img = Image.open(image_path)
                    contents.append(img)
                except Exception as e:
                    print(f"Error loading image for Gemini: {e}")
                    
            contents.append(prompt)
            
            models_to_try = [
                "gemini-3.8-flash",
                "gemini-3.7-flash",
                "gemini-3.5-flash-lite",
                "gemini-2.5-flash"
            ]
            last_err = None
            for model_name in models_to_try:
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=contents,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=0.7,
                            max_output_tokens=8192
                        )
                    )
                    if response and response.text:
                        return response.text
                except Exception as me:
                    last_err = me
                    continue
            if last_err:
                raise last_err
            return ""
        except Exception as e:
            raise ValueError(f"Lỗi gọi Google Gemini: {str(e)}. Hãy kiểm tra lại GEMINI_API_KEY tại https://aistudio.google.com/apikey")

    def _call_ai(self, prompt: str, image_path: Optional[str] = None, system_prompt: str = SYSTEM_INSTRUCTION) -> str:
        if self.provider == "gemini":
            if not self.gemini_key:
                raise ValueError("Chưa nhập GEMINI_API_KEY! Bạn có thể lấy key miễn phí tại https://aistudio.google.com/ và dán vào nút Cài Đặt (⚙️) phía trên.")
            return self._call_gemini(prompt, image_path, system_prompt)
        elif self.provider == "groq":
            if not self.groq_key:
                raise ValueError("Chưa nhập GROQ_API_KEY! Bạn có thể lấy key miễn phí tại https://console.groq.com/")
            return self._call_groq(prompt, system_prompt)
        else:
            if not self.openai_key:
                raise ValueError("Chưa nhập OPENAI_API_KEY! Vui lòng vào nút Cài Đặt (⚙️) để nhập key.")
            return self._call_openai(prompt, image_path, system_prompt)

    def generate_full_script_pipeline(
        self,
        topic: str,
        image_path: Optional[str] = None,
        video_type: str = "Video dài (16:9)",
        genre: str = "Bí ẩn / Ly kỳ",
        total_scenes: int = 55,
        progress_callback = None
    ) -> Dict[str, Any]:
        """
        Executes a 4-phase generation pipeline guaranteeing all 50-60 scenes:
        Phase 1: Part 1 - Kịch bản sườn & Tóm tắt nội dung chính.
        Phase 2: Part 2 - Scenes 1 to 20
        Phase 3: Part 2 - Scenes 21 to 40
        Phase 4: Part 2 - Scenes 41 to total_scenes
        """
        ar_tag = "--ar 16:9" if "16:9" in video_type else "--ar 9:16"
        pacing_rule = "4 đến 7 giây" if "16:9" in video_type else "3 đến 6 giây"

        if progress_callback:
            progress_callback(10, "Đang phân tích hình ảnh và tạo PHẦN 1: Kịch bản sườn & Tóm tắt nội dung chính...")

        # PHASE 1: Generate Outline & Sườn kịch bản
        prompt_phase1 = f"""
Bạn hãy phân tích kỹ bức ảnh được cung cấp (nếu có) và dựa vào chủ đề: "{topic}".
Thể loại / Mood: {genre}
Định dạng video: {video_type} (Aspect ratio tag: {ar_tag}, Nhịp độ mỗi cảnh: {pacing_rule})
Tổng số cảnh dự kiến: {total_scenes} cảnh.

HÃY VIẾT:
# PHẦN 1: KỊCH BẢN SƯỜN & TÓM TẮT NỘI DUNG CHÍNH


Yêu cầu cụ thể trong Phần 1:
1. TÓM TẮT CỐT TRUYỆN CHÍNH & THÔNG ĐIỆP:
   - Cốt truyện ngắn gọn, cuốn hút, nêu rõ mở đầu, mâu thuẫn, cao trào và bài học/thông điệp đọng lại.
2. PHÂN TÍCH HÌNH ẢNH GỐC & KHÓA PHONG CÁCH THỊ GIÁC (VISUAL & CHARACTER LOCK):
   - Phân tích nhân vật chính (gương mặt, tóc, độ tuổi, trang phục đặc trưng).
   - Phong cách mỹ thuật (Art style: cinematic 35mm, hyper-realistic, dramatic lighting, color palette).
   - Cụm từ khóa cố định (Consistency Prompt Anchor) để gắn vào tất cả các prompt tạo ảnh sau này.
3. THE 3-SECOND HOOK:
   - Visual Hook (Cú sốc thị giác cảnh mở màn): Mô tả chi tiết hình ảnh giật gân, đập vào mắt người xem.
   - Audio Interrupt (Cú sốc âm thanh): Mô tả hiệu ứng âm thanh ngắt quãng thói quen lướt video.
   - Curiosity Gap (Câu nói tò mò cực độ): Câu mở đầu không chào hỏi, đánh thẳng vào tâm lý hiếu kỳ.
4. YOUTUBE VIRAL PACKAGING:
   - 5 Tiêu đề giật gân kích thích CTR (không clickbait lừa dối nhưng khơi gợi tò mò tột độ).
   - 3 Ý tưởng Thumbnail (mô tả hình ảnh + Text Overlay 3-4 từ cực mạnh).
   - Mô tả video chuẩn SEO (kèm tóm tắt, hashtags, mốc timeline gợi ý).
5. SƯỜN MẠCH TRUYỆN PHÂN BỔ {total_scenes} CẢNH:
   - Hồi 1 (Cảnh 1 - 15): Khởi đầu bí ẩn & The 3-second hook
   - Hồi 2 (Cảnh 16 - 35): Thắt nút, khám phá và căng thẳng leo thang
   - Hồi 3 (Cảnh 36 - 48): Cao trào đỉnh điểm, bí mật kinh hoàng được giải mã
   - Hồi 4 (Cảnh 49 - {total_scenes}): Hậu quả, thông điệp sâu sắc và cái kết ám ảnh/kêu gọi hành động.

Hãy viết chi tiết, đẳng cấp, chuyên nghiệp theo đúng tinh thần Rule.txt!
"""
        part1_text = self._call_ai(prompt_phase1, image_path=image_path)

        # PHASE 2: Scenes 1 to 20
        if progress_callback:
            progress_callback(35, f"Đang sáng tác PHẦN 2: Chi tiết Cảnh 01 đến Cảnh 20 (Hook & Khởi đầu)...")

        prompt_phase2 = f"""
Dựa trên PHẦN 1 KỊCH BẢN SƯỜN đã xây dựng:
{part1_text[:2000]}

HÃY VIẾT:
# PHẦN 2: CHI TIẾT KỊCH BẢN ({total_scenes} PROMPT) - ĐỢT 1: TỪ CẢNH 01 ĐẾN CẢNH 20

YÊU CẦU BẮT BUỘC CHO TỪNG CẢNH (CẢNH 01 đến CẢNH 20):
- Tuân thủ nhịp độ {pacing_rule}, luân chuyển góc máy liên tục (Wide -> Close-up -> Low angle -> Over-the-shoulder).
- Cảnh 01 bắt buộc phải thực hiện chuẩn xác THE 3-SECOND HOOK (Visual Hook + Audio Interrupt + Curiosity Gap).
- Định dạng xuất chuẩn xác cho mỗi cảnh:

### [CẢNH xx] (Thời lượng: [3-6s/4-7s] | Góc máy: [Tên góc máy])
- **Prompt Tạo Ảnh (Midjourney v6 / Flux.1):**
  `[Viết bằng tiếng Anh chuẩn Prompt Engineering, gồm: Subject + Action + Camera Angle/Lens + Lighting + Style/Art aesthetic + Aspect Ratio tag {ar_tag}. Duy trì ngoại hình nhân vật nhất quán]`
- **Prompt Chuyển Động (Kling AI / Runway Gen-3 / Luma):**
  `[Chỉ dẫn chuyển động camera và môi trường, vd: Slow cinematic push in, subtle handheld shake, particle floating...]`
- **Voice-Over (Lời bình):**
  "[Chỉ dẫn ngữ điệu, vd: [thì thầm], [dồn dập], [ngắt nghỉ 1s]] Lời bình tiếng Việt tự nhiên, súc tích, giữ chân người xem."
- **Sound FX & BGM:**
  [Mô tả âm thanh, tiếng động, hiệu ứng âm thanh rùng rợn/kịch tính/tiết tấu nhanh]

Hãy viết đầy đủ từ CẢNH 01 đến CẢNH 20, không được bỏ sót cảnh nào!
"""
        batch1_text = self._call_ai(prompt_phase2)

        # PHASE 3: Scenes 21 to 40
        if progress_callback:
            progress_callback(60, f"Đang sáng tác PHẦN 2: Chi tiết Cảnh 21 đến Cảnh 40 (Cao trào & Thắt nút)...")

        prompt_phase3 = f"""
Tiếp tục kịch bản trên theo PHẦN 1.
Chủ đề: {topic} | Aspect ratio: {ar_tag} | Nhịp độ: {pacing_rule}
Đợt 1 vừa kết thúc ở Cảnh 20.

HÃY TIẾP TỤC VIẾT ĐỢT 2: TỪ CẢNH 21 ĐẾN CẢNH 40
Diễn biến: Mâu thuẫn leo thang, nhịp phim dồn dập, nguy hiểm bủa vây, những bí ẩn dần hé lộ.

Định dạng bắt buộc cho từng cảnh (CẢNH 21 đến CẢNH 40):
### [CẢNH xx] (Thời lượng: [xx s] | Góc máy: [xx])
- **Prompt Tạo Ảnh (Midjourney v6 / Flux.1):**
  `[Prompt tiếng Anh chuẩn Prompt Engineering + {ar_tag}]`
- **Prompt Chuyển Động (Kling AI / Runway Gen-3 / Luma):**
  `[Chỉ dẫn camera & movement]`
- **Voice-Over (Lời bình):**
  "[Chỉ dẫn ngữ điệu] Lời bình tiếng Việt sắc bén, nghẹt thở..."
- **Sound FX & BGM:**
  [Hiệu ứng âm thanh kịch tính]

Hãy viết đủ và chi tiết từ CẢNH 21 đến CẢNH 40!
"""
        batch2_text = self._call_ai(prompt_phase3)

        # PHASE 4: Scenes 41 to total_scenes
        if progress_callback:
            progress_callback(85, f"Đang sáng tác PHẦN 2: Chi tiết Cảnh 41 đến Cảnh {total_scenes} (Mở nút & Kết thúc)...")

        prompt_phase4 = f"""
Tiếp tục kịch bản trên theo PHẦN 1.
Chủ đề: {topic} | Aspect ratio: {ar_tag} | Nhịp độ: {pacing_rule}
Đợt 2 vừa kết thúc ở Cảnh 40.

HÃY TIẾP TỤC VIẾT ĐỢT 3: TỪ CẢNH 41 ĐẾN CẢNH {total_scenes}
Diễn biến: Đỉnh điểm cao trào, sự thật chấn động được phơi bày, hậu quả, cái kết ám ảnh và lời bình triết lý sâu sắc hoặc Call To Action ấn tượng.

Định dạng bắt buộc cho từng cảnh (CẢNH 41 đến CẢNH {total_scenes}):
### [CẢNH xx] (Thời lượng: [xx s] | Góc máy: [xx])
- **Prompt Tạo Ảnh (Midjourney v6 / Flux.1):**
  `[Prompt tiếng Anh chuẩn Prompt Engineering + {ar_tag}]`
- **Prompt Chuyển Động (Kling AI / Runway Gen-3 / Luma):**
  `[Chỉ dẫn camera & movement]`
- **Voice-Over (Lời bình):**
  "[Chỉ dẫn ngữ điệu] Lời bình tiếng Việt lắng đọng, ám ảnh..."
- **Sound FX & BGM:**
  [Hiệu ứng âm thanh kết thúc]

Hãy viết đầy đủ từ CẢNH 41 đến CẢNH {total_scenes}!
"""
        batch3_text = self._call_ai(prompt_phase4)

        if progress_callback:
            progress_callback(95, "Đang tổng hợp kịch bản và chuẩn hóa danh sách prompt...")

        # Combine into complete script
        full_markdown = f"{part1_text.strip()}\n\n---\n\n{batch1_text.strip()}\n\n{batch2_text.strip()}\n\n{batch3_text.strip()}"

        # Parse scenes into structured objects
        parsed_scenes = self.parse_scenes_from_text(full_markdown)

        if progress_callback:
            progress_callback(100, f"Hoàn tất xuất sắc {len(parsed_scenes)} cảnh kịch bản!")

        return {
            "topic": topic,
            "video_type": video_type,
            "genre": genre,
            "total_scenes": len(parsed_scenes),
            "part1_outline": part1_text,
            "full_markdown": full_markdown,
            "scenes": parsed_scenes
        }

    def parse_scenes_from_text(self, text: str) -> List[Dict[str, Any]]:
        """Parses markdown text into structured scene objects for UI and bulk export."""
        scenes = []
        # Match pattern: ### [CẢNH 01] or ### Cảnh 01 or ### [Scene 01] or ### SCENE 1
        scene_blocks = re.split(r'###?\s*\[?(?:CẢNH|CANH|SCENE)\s*(\d+)\]?', text, flags=re.IGNORECASE)
        
        if len(scene_blocks) > 1:
            for i in range(1, len(scene_blocks), 2):
                try:
                    scene_num = int(scene_blocks[i])
                except Exception:
                    continue
                block_content = scene_blocks[i+1]
                
                # Extract header line info (Duration, Camera)
                first_line = block_content.strip().splitlines()[0] if block_content.strip() else ""
                timing_match = re.search(r'(?:Thời lượng|Duration|Timing):\s*([^|)\n]+)', first_line, re.IGNORECASE)
                timing = timing_match.group(1).strip() if timing_match else "4s"
                
                camera_match = re.search(r'(?:Góc máy|Camera|Angle):\s*([^|)\n]+)', first_line, re.IGNORECASE)
                camera = camera_match.group(1).strip() if camera_match else "Cinematic"

                # Extract Image Prompt
                img_prompt = ""
                img_match = re.search(r'(?:Prompt Tạo Ảnh|Prompt Ảnh|Image Prompt|Midjourney)[^\n]*\n\s*`?([^`\n]+(?:(?:\n(?!-|\*|###)).+)*)`?', block_content, re.IGNORECASE)
                if not img_match:
                    img_match = re.search(r'(?:Prompt Tạo Ảnh|Prompt Ảnh|Image Prompt|Midjourney)[^:\n]*:\s*`?([^\n`]+)`?', block_content, re.IGNORECASE)
                if img_match:
                    img_prompt = img_match.group(1).strip().strip('`')

                # Extract Video Prompt
                vid_prompt = ""
                vid_match = re.search(r'(?:Prompt Chuyển Động|Prompt Video|Motion Prompt|Video Prompt)[^\n]*\n\s*`?([^`\n]+(?:(?:\n(?!-|\*|###)).+)*)`?', block_content, re.IGNORECASE)
                if not vid_match:
                    vid_match = re.search(r'(?:Prompt Chuyển Động|Prompt Video|Motion Prompt|Video Prompt)[^:\n]*:\s*`?([^\n`]+)`?', block_content, re.IGNORECASE)
                if vid_match:
                    vid_prompt = vid_match.group(1).strip().strip('`')

                # Extract Voice-Over
                voice_over = ""
                voice_match = re.search(r'(?:Voice-Over|Lời bình|Voiceover)[^\n]*\n\s*"?([^"\n]+(?:(?:\n(?!-|\*|###)).+)*)"?', block_content, re.IGNORECASE)
                if not voice_match:
                    voice_match = re.search(r'(?:Voice-Over|Lời bình|Voiceover)[^:\n]*:\s*"?(.*?)(?="\s*(?:\n|$)|(?:\n-|\n\*|\n###|$))', block_content, re.IGNORECASE | re.DOTALL)
                if voice_match:
                    voice_over = voice_match.group(1).strip().strip('"')

                # Extract Sound FX
                sfx = ""
                sfx_match = re.search(r'(?:Sound FX|Âm thanh|SFX|BGM)[^\n]*:\s*(.+?)(?=\n-|\n\*|\n###|$)', block_content, re.IGNORECASE | re.DOTALL)
                if sfx_match:
                    raw_sfx = sfx_match.group(1).strip()
                    raw_sfx = re.sub(r'^\*+\s*', '', raw_sfx)
                    raw_sfx = raw_sfx.strip('[] \n*')
                    sfx = raw_sfx

                scenes.append({
                    "scene_number": scene_num,
                    "timing": timing,
                    "camera": camera,
                    "image_prompt": img_prompt,
                    "video_prompt": vid_prompt,
                    "voiceover": voice_over,
                    "sound_fx": sfx,
                    "raw_text": f"### [CẢNH {scene_num:02d}]\n{block_content.strip()}"
                })
                
        return scenes
