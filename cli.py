import os
import sys
import argparse
import json
from pathlib import Path

# UTF-8 for console
sys.stdout.reconfigure(encoding='utf-8')

from ai_engine import ScriptGenerator
from config import OUTPUTS_DIR

def main():
    parser = argparse.ArgumentParser(description="AI YouTube Script Director (50-60 Prompt Generator)")
    parser.add_argument("--topic", "-t", required=True, help="Chủ đề hoặc ý tưởng kịch bản")
    parser.add_argument("--image", "-i", default=None, help="Đường dẫn file ảnh phân tích (tùy chọn)")
    parser.add_argument("--scenes", "-s", type=int, default=55, help="Số lượng cảnh/prompt (mặc định: 55)")
    parser.add_argument("--format", "-f", default="Video dài (16:9)", choices=["Video dài (16:9)", "Shorts / TikTok (9:16)"], help="Định dạng video")
    parser.add_argument("--genre", "-g", default="Bí ẩn / Ly kỳ", help="Thể loại kịch bản")
    parser.add_argument("--provider", "-p", default=None, choices=["openai", "gemini"], help="AI Provider (openai hoặc gemini)")
    parser.add_argument("--api-key", "-k", default=None, help="API Key")
    parser.add_argument("--output", "-o", default=None, help="Đường dẫn file markdown xuất ra (tùy chọn)")

    args = parser.parse_args()

    print("=" * 60)
    print("🎬 AI YOUTUBE SCRIPT DIRECTOR")
    print(f"Chủ đề: {args.topic}")
    print(f"Định dạng: {args.format} | Số cảnh: {args.scenes}")
    print(f"Ảnh phân tích: {args.image or 'Không có (Dùng chủ đề văn bản)'}")
    print("=" * 60)

    def print_progress(percent: int, message: str):
        print(f"[{percent:3d}%] {message}")

    gen = ScriptGenerator(provider=args.provider, api_key=args.api_key)
    try:
        result = gen.generate_full_script_pipeline(
            topic=args.topic,
            image_path=args.image,
            video_type=args.format,
            genre=args.genre,
            total_scenes=args.scenes,
            progress_callback=print_progress
        )

        # Save to file
        out_path = args.output
        if not out_path:
            clean_name = "".join(c for c in args.topic[:30] if c.isalnum() or c in (' ', '_', '-')).strip()
            out_path = OUTPUTS_DIR / f"{clean_name}.md"
        else:
            out_path = Path(out_path)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(result["full_markdown"])

        # Also save JSON for machine parsing
        json_path = out_path.with_suffix(".json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print("\n" + "=" * 60)
        print(f"✅ ĐÃ TẠO THÀNH CÔNG {len(result['scenes'])} CẢNH!")
        print(f"📄 File Markdown: {out_path}")
        print(f"📊 File JSON:     {json_path}")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
