# TOOL KỊCH BẢN VIDEO AI YOUTUBE (50-60 PROMPT)

> **Tuân thủ tuyệt đối quy chuẩn tại `Rule.txt`**: Thiết kế chuyên biệt cho nhà sản xuất video YouTube AI & Shorts, tạo ra kịch bản hoàn chỉnh chuẩn Hollywood gồm đúng 2 phần:
> 1. **Phần 1:** Kịch bản sườn & Tóm tắt nội dung chính (Cốt truyện, Khóa nhân vật, The 3-Second Hook, 5 Tiêu đề CTR cao, 3 Ý tưởng Thumbnail, SEO).
> 2. **Phần 2:** Chi tiết kịch bản gồm **50 đến 60 cảnh / prompt** (Đầy đủ Prompt Midjourney/Flux tiếng Anh, Prompt Motion Kling/Runway, Lời bình Voice-Over giàu cảm xúc và Sound FX).

---

## ⚡ HƯỚNG DẪN KÍCH HOẠT GOOGLE GEMINI MIỄN PHÍ 100%

Công cụ đã được cấu hình mặc định sử dụng **Google Gemini** (mô hình `gemini-2.5-flash`), hoàn toàn miễn phí từ Google với hạn mức cực lớn (1.500 lượt tạo kịch bản/ngày, hỗ trợ phân tích hình ảnh đa phương thức siêu tốc):

1. **Lấy API Key miễn phí (mất 10 giây):**
   - Truy cập trang chính thức: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
   - Đăng nhập tài khoản Google của bạn $\rightarrow$ bấm **Create API Key**.
   - Copy đoạn mã API Key (bắt đầu bằng `AIzaSy...`).

2. **Dán Key vào công cụ:**
   - **Cách 1 (Ngay trên giao diện Web):** Khởi động tool, dán key vào ô xanh ở góc trái màn hình rồi bấm **Lưu Key**.
   - **Cách 2 (Lưu trực tiếp vào file):** Mở file `.env` tại thư mục này, dán key vào dòng:
     ```env
     DEFAULT_PROVIDER=gemini
     GEMINI_API_KEY=AIzaSy... (dán key của bạn vào đây)
     ```

---

## 🚀 HƯỚNG DẪN KHỞI ĐỘNG (1-CLICK)

### Cách 1: Khởi động giao diện Web trực quan (Khuyên dùng)
- **Nhấp đúp chuột vào file:** `Chay_Tool.bat`
- Công cụ sẽ tự động kích hoạt máy chủ cục bộ và tự mở trình duyệt web tại địa chỉ: `http://127.0.0.1:8000`

### Cách 2: Khởi động qua dòng lệnh (Terminal / PowerShell)
```powershell
cd C:\Users\Public\Documents\Tool-Kichban
python server.py
```

### Cách 3: Chạy nhanh qua giao diện dòng lệnh (CLI Mode)
```powershell
python cli.py --topic "Bí mật lăng mộ Tần Thủy Hoàng và đội quân đất nung" --scenes 55 --format "Video dài (16:9)"
```
*(Hoặc kèm ảnh: `python cli.py --topic "..." --image "character.jpg" --scenes 60`)*

---

## 🎯 CÁC TÍNH NĂNG VƯỢT TRỘI

1. **Phân tích hình ảnh thông minh (Multimodal Vision):**
   - Phân tích kỹ lưỡng bức ảnh bạn cung cấp (gương mặt nhân vật, trang phục, phong cách mỹ thuật, góc máy, ánh sáng).
   - Tự động tạo cụm từ khóa cố định (**Consistency Prompt Anchor**) và chèn vào toàn bộ 50-60 cảnh để giữ nhân vật và mỹ thuật đồng nhất 100%.

2. **Cơ chế Pipeline 4 đợt (Đảm bảo đủ 50-60 cảnh không bị ngắt quãng):**
   - AI truyền thống khi viết 50-60 cảnh thường bị nghẽn token ở cảnh 20-30.
   - Tool áp dụng quy trình sản xuất điện ảnh 4 đợt (Sườn kịch bản -> Cảnh 1-20 -> Cảnh 21-40 -> Cảnh 41-60), đảm bảo **100% đủ từ cảnh 01 đến cảnh cuối**, không thiếu một chi tiết nào.

3. **Giao diện làm việc chuyên nghiệp (Studio Dashboard):**
   - **Thẻ phân cảnh (Scene Cards):** Mỗi cảnh hiển thị thời lượng (3-6s), góc máy, Prompt ảnh, Prompt video, Lời bình và Sound FX.
   - **Nút Copy 1-Click:** Copy nhanh Prompt Midjourney, Prompt Kling hoặc Voice-over.
   - **Xuất hàng loạt (Bulk Export):**
     * Xuất danh sách Prompt ảnh (mỗi dòng 1 prompt) dán thẳng vào Discord/Midjourney.
     * Xuất toàn bộ Lời bình Voice-over cho ElevenLabs / CapCut.
     * Tải file bảng tính **Excel / CSV (UTF-8 BOM)**.
     * Tải file Markdown (.md) toàn văn bản.

4. **Hỗ trợ cả OpenAI & Google Gemini:**
   - Đã tích hợp sẵn API Key trong file `.env`.
   - Có thể cấu hình hoặc đổi key trực tiếp ngay trên giao diện Web (Nút Cài đặt góc trên cùng bên phải).

---

## 📋 CẤU TRÚC ĐẦU RA THEO ĐÚNG RULE.TXT

```markdown
# PHẦN 1: KỊCH BẢN SƯỜN & TÓM TẮT NỘI DUNG CHÍNH
- 1. Tóm tắt cốt truyện chính & Thông điệp
- 2. Phân tích hình ảnh gốc & Khóa phong cách thị giác (Visual & Character Lock)
- 3. The 3-Second Hook (Visual Hook + Audio Interrupt + Curiosity Gap)
- 4. YouTube Viral Packaging (5 Tiêu đề giật gân CTR cao + 3 Thumbnail + Mô tả SEO)
- 5. Sườn mạch truyện phân bổ 50-60 cảnh

---

# PHẦN 2: CHI TIẾT KỊCH BẢN (50 - 60 PROMPT)
### [CẢNH 01] (Thời lượng: 4s | Góc máy: Extreme Close-up)
- **Prompt Tạo Ảnh (Midjourney v6 / Flux.1):**
  `Subject + Action + Camera Angle/Lens + Lighting + Style + --ar 16:9`
- **Prompt Chuyển Động (Kling AI / Runway Gen-3 / Luma):**
  `[Chỉ dẫn chuyển động camera và môi trường]`
- **Voice-Over (Lời bình):**
  "[thì thầm] Câu mở đầu bí ẩn kích thích tò mò tột độ..."
- **Sound FX & BGM:**
  [Hiệu ứng âm thanh giật mình / dồn dập]

... (kéo dài liên tục tới CẢNH 55 - 60)
```

---

## 📁 CẤU TRÚC THƯ MỤC DỰ ÁN

```
C:\Users\Public\Documents\Tool-Kichban\
│
├── Rule.txt              # Bộ quy tắc đạo diễn YouTube chuẩn quốc tế
├── Chay_Tool.bat         # File chạy 1-click mở giao diện Web
├── server.py             # Máy chủ FastAPI & API Streaming
├── ai_engine.py          # Bộ điều phối AI Pipeline 4 đợt & Trích xuất Scene
├── cli.py                # Công cụ chạy dòng lệnh (Terminal)
├── config.py             # Quản lý cấu hình & biến môi trường
├── .env                  # Lưu trữ API Key (OpenAI / Gemini)
│
├── static/               # Giao diện Web Dark Mode cao cấp
│   ├── index.html        # Giao diện chính
│   ├── app.js            # Xử lý tương tác, upload ảnh, SSE streaming
│   └── style.css         # Hiệu ứng CSS & Dark theme
│
├── uploads/              # Thư mục lưu ảnh người dùng tải lên
└── outputs/              # Thư mục tự động lưu trữ các kịch bản (.md, .json)
```
