import json
from pathlib import Path
from ai_engine import ScriptGenerator

BASE_DIR = Path(__file__).resolve().parent
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

topic = "Bí Mật Lăng Mộ Tần Thủy Hoàng: Đội Quân Đất Nung Và Biển Thủy Ngân Vĩnh Cửu"

part1_outline = """# PHẦN 1: KỊCH BẢN SƯỜN & TÓM TẮT NỘI DUNG CHÍNH

### 1. TÓM TẮT CỐT TRUYỆN CHÍNH & THÔNG ĐIỆP
- **Cốt truyện:** Sau hơn 2.200 năm, lăng mộ của Hoàng đế đầu tiên Trung Hoa - Tần Thủy Hoàng vẫn là một trong những bí ẩn lớn nhất của nhân loại mà không nhà khảo cổ nào dám khai quật hoàn toàn. Bộ phim AI đưa người xem thâm nhập sâu vào lòng đất Ly Sơn, đối mặt với đội quân đất nung canh giữ giấc ngủ ngàn năm, mê cung cạm bẫy nỏ tự động và một thế giới ngầm được mô phỏng với sông biển bằng thủy ngân nguyên chất kịch độc.
- **Thông điệp cốt lõi:** Khao khát sự trường sinh bất tử của con người dù có quyền lực tột đỉnh đến đâu cũng chỉ tạo ra những bi kịch vĩnh hằng giam cầm trong bóng tối.

### 2. PHÂN TÍCH HÌNH ẢNH GỐC & KHÓA PHONG CÁCH THỊ GIÁC (VISUAL & CHARACTER LOCK)
- **Nhân vật trung tâm:** 
  + Hoàng đế Tần Thủy Hoàng trong y phục hoàng tộc đen - vàng viền rồng cổ đại (Qin dynasty black imperial robe with intricate gold embroidery), ánh mắt uy nghiêm, sắc lạnh, đội mũ miện miên lưu (imperial beaded crown).
  + Đội quân chiến binh đất nung (Terracotta warrior army): Giáp phiến đá, nét mặt đanh thép phong hóa theo thời gian.
- **Bối cảnh & Mỹ thuật:** Mê cung ngầm thời Tần, cột trụ đá khắc phù điêu cổ đại, sông thủy ngân phát sáng ánh kim bạc ma mị, khói sương mờ ảo, ngọn đuốc dầu cá voi cháy mãi không tắt.
- **Bảng màu & Ánh sáng:** Dark cinematic palette, gold accents, cyan reflections from liquid mercury, volumetric light rays, deep obsidian shadows.
- **Cụm từ khóa khóa phong cách (Consistency Anchor):** 
  `Qin dynasty aesthetic, Qin Shi Huang imperial armor, terracotta warriors, liquid mercury rivers, volumetric cinematic lighting, 35mm film photography, 8k hyper-realistic --ar 16:9`

### 3. THE 3-SECOND HOOK (MỞ ĐẦU NGHẸT THỞ)
- **Visual Hook (Cú sốc thị giác):** Cận cảnh macro một bức tượng chiến binh đất nung nứt toác, từ bên trong một con mắt sống bằng đồng thau chuyển động dữ dội, rỉ ra dòng thủy ngân lỏng sáng bạc.
- **Audio Pattern Interrupt (Cú sốc âm thanh):** Tiếng thở hắt hoảng loạn cắt ngang tiếng nứt vỡ rợn người của đất nung, bùng nổ cú đập bass sub-bass chấn động màng nhĩ.
- **Curiosity Gap (Câu mở đầu kích thích tò mò):** "[thì thầm dồn dập] Đừng tin vào sách sử! 8.000 tượng đất nung này... chưa từng được tạo ra để tưởng niệm người chết, mà là để GIAM CẦM một thứ gì đó!"

### 4. YOUTUBE VIRAL PACKAGING
- **5 Tiêu Đề Kích Thích CTR:**
  1. Bí Ẩn Kinh Hoàng Trong Lăng Mộ Tần Thủy Hoàng: Vì Sao 2.200 Năm Không Ai Dám Khai Quật?
  2. Sự Thật Đáng Sợ Dưới Biển Thủy Ngân Lăng Mộ Tần Thủy Hoàng!
  3. Thứ Đang Ngủ Yên Dưới 8.000 Tượng Đất Nung Không Phải Là Một Vị Vua!
  4. Giải Mã Cạm Bẫy Chết Người Trong Lăng Mộ Bí Ẩn Nhất Lịch Sử Nhân Loại
  5. Phát Hiện Chấn Động: Điều Gì Thực Sự Được Chôn Cùng Tần Thủy Hoàng?
- **3 Ý Tưởng Thumbnail:**
  - *Ý tưởng 1:* Cận cảnh nửa mặt tượng đất nung bị vỡ, để lộ ánh mắt quỷ dị phát sáng vàng kim. Text Overlay: **"ĐỪNG KHAI QUẬT!"**
  - *Ý tưởng 2:* Đội quân đất nung xếp hàng vô tận, giữa tâm là dòng sông thủy ngân tím ma mị và chiếc quan tài đồng lơ lửng. Text Overlay: **"BÍ MẬT 2200 NĂM"**
  - *Ý tưởng 3:* Nhà khảo cổ cầm đèn pin chiếu vào cửa mộ bị nỏ tự động bắn xuyên. Text Overlay: **"CẠM BẪY CHẾT NGƯỜI"**
- **Mô tả SEO Video:**
  Tần Thủy Hoàng thống nhất lục quốc, đốt sách chôn nho và để lại công trình lăng mộ vĩ đại nhưng đầy ma mị dưới chân núi Ly Sơn. Video này hé lộ phân tích toàn diện về bí ẩn sông thủy ngân, hệ thống nỏ tự động bắn liên hoàn, và giả thuyết chấn động về mục đích thực sự của 8.000 chiến binh đất nung.
  #TanThuyHoang #BiAnLichSu #TerracottaArmy #LangMoCoDai #KhamPhaBiAn

### 5. SƯỜN MẠCH TRUYỆN PHÂN BỔ 55 CẢNH
- **Hồi 1 (Cảnh 01 - 15):** The 3-second hook, phát hiện chấn động năm 1974 tại Tây An, sự sợ hãi của các nhà khảo cổ trước lời nguyền cổ đại.
- **Hồi 2 (Cảnh 16 - 32):** Thâm nhập mê cung ngầm, khảo sát hệ thống cạm bẫy nỏ tự động và nồng độ thủy ngân cao bất thường gấp hàng trăm lần.
- **Hồi 3 (Cảnh 33 - 47):** Khám phá cung điện ngầm, dòng sông ngân hà bằng thủy ngân nguyên chất, bí mật khao khát bất tử và những chén thuốc trường sinh độc dược.
- **Hồi 4 (Cảnh 48 - 55):** Vì sao công nghệ hiện đại vẫn chùn bước không dám mở nắp quan tài; thông điệp triết lý về thời gian, quyền lực và cái chết.
"""

# Let's generate 55 scenes programmatically with rich content conforming strictly to Rule.txt!
scenes_data = []

# List of 55 scenes meticulously planned
scene_plans = [
    # Act 1: Scenes 1-15 (Hook & Mystery)
    (1, "4s", "Extreme Close-up",
     "Macro cinematic shot of an ancient terracotta warrior face cracking, silver metallic liquid mercury slowly weeping from the fissure, dramatic chiaroscuro lighting, 8k, hyper-detailed --ar 16:9",
     "Slow cinematic push-in towards the fissure, subtle particle of dust drifting, silver liquid reflecting torchlight",
     "[thì thầm dồn dập] Đừng tin vào những gì sách giáo khoa kể cho bạn! 8.000 bức tượng đất nung này...",
     "Tiếng gốm nung nứt toác sắc lẹm, âm bass dội sâu thăm thẳm"),
    
    (2, "4s", "Wide Shot / Low angle",
     "Epic wide low-angle shot of endless rows of 8,000 terracotta warriors standing in underground pit, eerie torchlight, heavy volumetric atmospheric fog, cinematic film still --ar 16:9",
     "Smooth dynamic crane lift, shadows flickering against carved stone walls",
     "[ngắt nghỉ 1s] [trầm lạnh] ...chưa từng được tạo ra để tôn vinh một người chết!",
     "Tiếng hàng ngàn bước chân kim loại trầm mặc vọng từ lòng đất"),

    (3, "5s", "Medium Shot",
     "Terracotta warrior commander holding ancient bronze sword, lifeless stone eyes staring forward, cobwebs in hollow armor, dark moody shadows --ar 16:9",
     "Slow rotational camera orbit around the stone commander, flickering candle flame reflection",
     "[nhấn mạnh] Mà là để GIAM CẦM... một thứ kinh hoàng không được phép thức giấc!",
     "Tiếng kim loại ma sát chói gắt, tiếng gió rít qua khe đá hẹp"),

    (4, "4s", "Establishing Shot",
     "Misty aerial shot of Mount Li in Shaanxi China at twilight, overcast stormy sky, ancient mystical landscape, cinematic drone shot --ar 16:9",
     "Slow forward drone descent toward the forested mountain slopes, dark clouds rolling",
     "[chậm rãi] Mùa xuân năm 1974, những người nông dân Tây An trong lúc đào giếng...",
     "Tiếng cuốc chim bổ vào đá cằn khô khốc"),

    (5, "4s", "Close-up",
     "An ancient bronze shovel strikes hard soil, breaking through into an pitch black subterranean void, dust billowing upward, flashlight beam cutting darkness --ar 16:9",
     "Quick camera punch-in as soil collapses into darkness, dust particles swirling in flashlight beam",
     "[dồn dập] ...đã vô tình phá vỡ phong ấn được chôn sâu suốt hơn hai thiên niên kỷ!",
     "Tiếng đất đá sụp đổ rào rào, tiếng thở dốc kinh ngạc"),

    (6, "5s", "Over-the-shoulder",
     "Shocked archaeologist in 1970s attire shining lantern into newly opened tomb cavern, revealing hundreds of life-sized terracotta soldiers staring back, wide eyes --ar 16:9",
     "Subtle handheld camera shake capturing trembling hands, light beam panning across stone faces",
     "[thì thầm] Trước mắt họ: hàng ngàn gương mặt đá... mỗi người mang một nét mặt khác biệt hoàn toàn.",
     "Âm thanh hợp xướng u linh thì thầm ma quái"),

    (7, "4s", "Macro Close-up",
     "Extreme close up of terracotta warrior ear and lips, showing realistic skin pores and hair strands sculpted in baked clay, ancient pigments fading --ar 16:9",
     "Slow lateral pan across the sculpted face, faint pigment flakes peeling in slow motion",
     "[nghi vấn] Không có hai bức tượng nào giống nhau. Phải chăng...",
     "Tiếng thì thầm hư ảo như tiếng người thở nhẹ"),

    (8, "4s", "Dramatic Close-up",
     "Flickering shadow of a living Qin dynasty soldier superimposed over terracotta clay mold, molten bronze casting, intense red fire glow --ar 16:9",
     "Morph transition between living human face and cold stone statue face, glowing ember particles",
     "[dồn dập] ...người ta đã đúc tượng sống từ những binh sĩ bằng da bằng thịt?",
     "Tiếng búa đập đe thép chan chát, tiếng lửa gầm réo"),

    (9, "5s", "Wide Shot",
     "X-ray forensic scan of terracotta statues in modern high-tech laboratory, blue luminescent wireframe revealing hollow clay interiors, scientists analyzing monitors --ar 16:9",
     "Smooth digital camera pan across glowing holographic wireframe render",
     "[khoa học] Khoa học hiện đại đã chứng minh bên trong rỗng ruột. Nhưng điều đó lại mở ra một câu hỏi còn đáng sợ hơn:",
     "Tiếng máy móc điện tử bíp ngắt quãng, âm thanh máy quét cộng hưởng"),

    (10, "5s", "Low angle",
     "Towering bronze statue of Emperor Qin Shi Huang standing atop pyramid palace steps, wearing ornate black robes with golden dragon motifs, imperial crown beads hanging --ar 16:9",
     "Low angle slow tilt-up towards the emperor cold eyes, royal banners fluttering in subterranean draft",
     "[uy quyền] Tại sao một hoàng đế thống nhất cả thiên hạ lại ám ảnh về cái chết đến mức điên cuồng như vậy?",
     "Tiếng trống trận rền vang xa xăm, tiếng tù và cổ đại"),

    (11, "4s", "Wide Panoramic",
     "Ancient Chinese battlefield with thousands of Qin soldiers with crossbows, burning siege engines, dramatic sunset sky, battlefield carnage, epic cinematography --ar 16:9",
     "Epic cinematic camera pull back revealing the vast conquest of the Six Kingdoms",
     "[dồn dập] Sau khi tiêu diệt sáu nước, thâu tóm mọi quyền lực trong tay...",
     "Tiếng binh khí va chạm rền trời, tiếng hò reo chiến trận"),

    (12, "4s", "Medium Shot",
     "Aging Emperor Qin Shi Huang looking into a polished bronze mirror by dim candlelight, seeing white hair and wrinkles, eyes filled with terror and fury --ar 16:9",
     "Slow push in on the emperor reflection, trembling hands touching hollow cheeks",
     "[thì thầm chua xót] ...Tần Thủy Hoàng nhận ra kẻ thù lớn nhất mà ông không thể đánh bại: chính là THỜI GIAN.",
     "Tiếng đồng hồ cát chảy róc rách, tiếng tim đập chậm dần"),

    (13, "5s", "Close-up",
     "Court alchemist in dark Hanfu robes grinding cinnabar and liquid mercury in a stone mortar, glowing vapors rising, mysterious ancient Daoist scrolls --ar 16:9",
     "Slow motion focus shift from pestle grinding red powder to shimmering liquid mercury pool",
     "[bí hiểm] Những phương sĩ, đạo sĩ từ khắp phương trời dâng lên những viên đan dược 'trường sinh'.",
     "Tiếng chất lỏng sôi sùng sục, tiếng giọt thủy ngân rơi tí tách"),

    (14, "4s", "Macro Shot",
     "Golden ornate chalice filled with shimmering silver liquid mercury and red cinnabar elixir, reflecting ominous candle glow, extreme depth of field --ar 16:9",
     "Macro slow cinematic tilt down into the silver metallic swirling surface",
     "[nghiệt ngã] Nhưng thứ họ gọi là 'thần dược'... thực chất lại là kim loại độc hại nhất trần gian: THỦY NGÂN.",
     "Âm thanh kim loại rít nhẹ, tiếng thở nghẹt thở"),

    (15, "5s", "Dramatic Wide",
     "Emperor Qin Shi Huang collapsing on imperial chariot during his final eastern inspection tour, royal guards panicking in sandstorm, imperial convoy halted --ar 16:9",
     "Dramatic handheld tracking shot running through dust storm towards the imperial carriage",
     "[dồn dập] Năm 210 trước Công Nguyên, vị bạo chúa đột tử trên đường tuần du, để lại bản kế hoạch lăng mộ kinh hoàng nhất lịch sử nhân loại!",
     "Tiếng sét xé rách bầu trời, tiếng ngựa hí hỗn loạn"),

    # Act 2: Scenes 16-32 (Subterranean Palace & Lethal Traps)
    (16, "5s", "Wide Shot",
     "Cutaway architectural illustration of the massive multi-layered underground pyramid mausoleum under Mount Li, subterranean rivers, trap chambers, glowing core --ar 16:9",
     "3D digital fly-through penetrating down through subterranean layers of rock and timber",
     "[chậm rãi] Sâu 35 mét dưới lòng đất, một 'thành phố của người chết' được xây dựng bởi hơn 700.000 nô lệ suốt 38 năm ròng rã.",
     "Âm thanh máy đo địa chấn rền rĩ, tiếng đục đẽo đá ngàn năm"),

    (17, "4s", "Medium Shot",
     "Ancient Chinese laborers hauling massive granite blocks under whips of guards in torchlit underground tunnels, dust choked air, intense contrast --ar 16:9",
     "Tracking shot moving alongside exhausted laborers pushing giant stone wheels",
     "[đau thương] Hàng vạn sinh mạng đã vĩnh viễn nằm lại bên dưới những phiến đá này.",
     "Tiếng xích sắt kéo lê trên đá, tiếng roi quất chan chát"),

    (18, "5s", "Close-up",
     "Heavy stone door sealing shut with massive iron chains and molten copper poured into seams, trapping workers inside darkness, lantern going out --ar 16:9",
     "Violent camera shake as stone slabs slam together, total darkness engulfing the frame",
     "[ngắt nghỉ 1s] [thì thầm lạnh gáy] Sau khi an táng hoàng đế, toàn bộ thợ thủ công đều bị nhốt sống bên trong để vĩnh viễn giữ kín bí mật đường hầm.",
     "Cú 'RẦM' dội của cánh cổng đá khép lại, tiếng kêu cứu nghẹn lại trong gang tấc"),

    (19, "4s", "First Person POV",
     "First person POV entering ancient subterranean stone corridor, flashlight illuminating tripwires and concealed wall slits, ominous shadows --ar 16:9",
     "Handheld slow walking movement, dust suspended in flashlight beam, subtle bobbing",
     "[hồi hộp] Nếu ai đó bước chân vào đây... họ sẽ đối mặt với điều gì?",
     "Tiếng bước chân dẫm lên cát vụn, tiếng tim đập thình thịch"),

    (20, "4s", "Extreme Close-up",
     "Intricate ancient bronze mechanical gear trigger hidden in tomb floor tiles, pressure plate clicking downward, bronze spring loading --ar 16:9",
     "Macro high-speed shot of gear teeth locking and mechanical bronze release clicking",
     "[dồn dập] CẠM BẪY NỎ TỰ ĐỘNG! Sử sách cổ ghi lại: hễ có kẻ xâm nhập, nỏ thần sẽ tự động bắn ra liên hoàn!",
     "Tiếng 'CẠCH' khô khốc của cò bẫy vừa kích hoạt"),

    (21, "4s", "Action Shot",
     "Volley of hundreds of bronze arrows flying from dark wall slits in extreme slow motion, bronze arrowheads coated in deadly venom, glowing torchlight --ar 16:9",
     "Slow-motion tracking shot following a lethal bronze arrow slicing through darkness",
     "[nghẹt thở] Những mũi tên đồng này được tôi luyện với độc dược, đủ sức xuyên thủng mọi lớp áo giáp trong tích tắc!",
     "Tiếng rít xé gió 'VÙ VÙ' của hàng trăm mũi tên lao tới"),

    (22, "5s", "Macro Shot",
     "Laboratory microscope shot of excavated Qin dynasty bronze arrowheads, preserved for 2,200 years without rust due to chromium coating, razor sharp edge --ar 16:9",
     "Smooth macro rotational zoom along the polished bronze cutting edge",
     "[khoa học kinh ngạc] Đáng kinh ngạc là các mũi tên khai quật được vẫn sáng loáng, sắc lẹm nhờ lớp mạ crom chống gỉ đi trước thế giới cả hai nghìn năm!",
     "Tiếng kim loại vang lên thanh thoát, sắc lẹm"),

    (23, "4s", "Medium Shot",
     "Archaeologist in protective biohazard hazmat suit using ground-penetrating radar on top of Mount Li mound, laptop screen displaying underground thermal anomalies --ar 16:9",
     "Slow pan from archaeologist face-shield to glowing radar heat-map on screen",
     "[nghiêm túc] Nhưng cạm bẫy vật lý vẫn chưa phải là thứ đáng sợ nhất.",
     "Tiếng bíp bíp dồn dập của máy đo phóng xạ và khí độc"),

    (24, "5s", "Wide Shot",
     "Scientists taking soil and air core samples around the mound, red hazard warnings on monitors showing extreme toxic spikes --ar 16:9",
     "Dynamic tracking shot around scientific drilling equipment, steam venting",
     "[dồn dập] Khi các nhà khoa học lấy mẫu đất tại gò mộ, họ phát hiện nồng độ thủy ngân cao gấp 280 lần mức bình thường!",
     "Tiếng còi cảnh báo nồng độ độc hại vang rền"),

    (25, "5s", "Atmospheric Wide",
     "Subterranean cavern showing silver liquid mercury droplets condensing on ancient stone vault ceiling, dripping into pool below, toxic fumes, surreal glow --ar 16:9",
     "Slow tilt up to stone ceiling studded with pearls and silver droplets hanging like stars",
     "[thì thầm rợn người] Sử ký Tư Mã Thiên đã không hề phóng đại khi viết:",
     "Tiếng giọt kim loại nặng rơi 'Tõm... tõm' vào vũng sâu"),

    (26, "5s", "Epic Panoramic",
     "Underground vast miniature continent inside mausoleum, flowing glowing silver rivers of liquid mercury representing Yangtze and Yellow Rivers, bronze miniature mountains --ar 16:9",
     "Sweeping epic drone shot flying low over the reflective liquid mercury river system",
     "[hùng tráng pha rùng rợn] 'Lấy thủy ngân làm trăm con sông, sông Hoàng Hà, sông Trường Giang và biển lớn, dùng máy móc cơ quan làm cho nước chảy không ngừng.'",
     "Âm thanh sóng nước kim loại nặng dâng trào cuồn cuộn"),

    (27, "4s", "Macro Close-up",
     "Vast pool of mirror-like liquid mercury reflecting floating bronze islands and miniature castles, ripples moving across surface mechanically --ar 16:9",
     "Close orbit shot around bronze mechanical paddle wheel churning silver liquid",
     "[sâu sắc] Ước tính có tới hơn 100 tấn thủy ngân nguyên chất đang lưu chuyển ngày đêm dưới chân núi Ly Sơn!",
     "Tiếng guồng nước kim loại kẽo kẹt quay đều"),

    (28, "5s", "Low angle",
     "Vaulted dome ceiling of the tomb chamber painted in deep indigo, studded with thousands of luminous sea pearls depicting constellations and astrological charts --ar 16:9",
     "Mesmerizing slow rotational view looking straight up at the pearlescent galaxy ceiling",
     "[huyền bí] Trên vòm trần là cả một bầu trời sao thiên văn bằng ngọc trai phát sáng vĩnh viễn nhờ dầu mỡ cá voi cháy mãi.",
     "Tiếng gió lùa qua vòm đá như bản giao hưởng vũ trụ"),

    (29, "4s", "Close-up",
     "Ancient bronze perpetual lantern shaped like a mermaid, holding flame fueled by mystic whale oil, burning in absolute silence --ar 16:9",
     "Slow macro push into the golden flame dancing over dark bronze features",
     "[thì thầm] Tần Thủy Hoàng đã tái tạo toàn bộ vũ trụ và giang sơn của mình ngay trong lòng đất...",
     "Tiếng lửa lách tách nhỏ giọt cô đơn"),

    (30, "4s", "Wide Shot",
     "A giant golden imperial sarcophagus resting on a floating bronze boat drifting slowly in the center of the liquid mercury ocean, shrouded in mystical mist --ar 16:9",
     "Slow majestic tracking shot through heavy silver fog toward the floating sarcophagus",
     "[trang nghiêm] ...để tiếp tục làm Hoàng đế cai trị cõi vĩnh hằng!",
     "Tiếng chuông đồng ngân nga trầm mặc kéo dài"),

    (31, "5s", "Medium Shot",
     "Modern 3D laser lidar subterranean scan rendering a digital wireframe of the central burial chamber, millions of green data points revealing coffin structure --ar 16:9",
     "Fast orbit around holographic lidar cloud data revealing hidden inner chambers",
     "[nghi vấn] Nhưng liệu bên trong cỗ quan tài đó... thi hài Tần Thủy Hoàng có còn nguyên vẹn?",
     "Tiếng quét radar kỹ thuật số chạy dồn dập"),

    (32, "4s", "Close-up",
     "Forensic reconstruction of Emperor Qin Shi Huang face on computer screen, sharp intense eyes, pale countenance, royal jade hairpin --ar 16:9",
     "Subtle camera pan across digital facial reconstruction monitor",
     "[tò mò] Hay thi hài của vị vua đã bị phân hủy bởi chính chất độc thủy ngân mà ông tôn sùng?",
     "Âm thanh hồi hộp nghẹt thở ngưng đọng"),

    # Act 3: Scenes 33-47 (The Real Mystery & Modern Dilemma)
    (33, "5s", "Wide Shot",
     "Excavation trench Pit 1 in Xian, showing archaeologists in white suits painstakingly brushing dirt from freshly uncovered terracotta soldier with vibrant purple paint --ar 16:9",
     "Slow crane shot moving down into the archaeological trench alongside conservators",
     "[dồn dập] Nhiều người thắc mắc: Với công nghệ thế kỷ 21, tại sao Trung Quốc vẫn KIÊN QUYẾT không mở nắp lăng mộ?",
     "Tiếng chổi quét đất nhẹ nhàng sột soạt"),

    (34, "4s", "Extreme Close-up",
     "Vibrant Han purple and crimson pigment on newly excavated terracotta soldier face curling, oxidizing and turning dull gray within 15 seconds of air exposure --ar 16:9",
     "Time-lapse style fast oxidation, brilliant colors fading into drab gray mud in seconds",
     "[tiếc nuối] Câu trả lời nằm ở thảm kịch xảy ra năm 1974. Những bức tượng ban đầu vốn có màu sắc rực rỡ tuyệt mỹ...",
     "Âm thanh tiếng rít oxy hóa khô héo đau đớn"),

    (35, "4s", "Close-up",
     "Archaeologist watch in horror as ancient 2,000-year-old painted terracotta armor turns monochrome in front of their eyes, camera capturing desperation --ar 16:9",
     "Handheld close up on trembling hands trying in vain to shield statue from air",
     "[xót xa] ...nhưng chỉ trong vòng 15 giây tiếp xúc với không khí, toàn bộ lớp sơn cổ đại đã bị oxy hóa và bong tróc vĩnh viễn!",
     "Tiếng thở dài bất lực xót xa"),

    (36, "5s", "Historical Flashback",
     "Archival footage style of 1956 excavation of Dingling Ming dynasty tomb, precious silk robes of Emperor Wanli crumbling into ash upon air contact --ar 16:9",
     "Desaturated sepia tone footage, silk disintegrating into dust in slow motion",
     "[bài học lịch sử] Bài học đau đớn từ lăng Định Lăng thời Minh: Những bảo vật nghìn năm bằng lụa và gỗ đã biến thành tro bụi chỉ sau vài phút mở cửa.",
     "Tiếng bụi tro bay xào xạc theo làn gió"),

    (37, "4s", "Macro Shot",
     "Modern laboratory environmental preservation chamber with nitrogen gas valves, airtight glass container protecting an artifact --ar 16:9",
     "Tracking shot along pressurized nitrogen gas tubes and humidity gauges",
     "[khẳng định] Nếu mở lăng mộ Tần Thủy Hoàng lúc này, những bích họa và di vật vô giá sẽ bị hủy hoại trước khi kịp nghiên cứu!",
     "Tiếng xì hơi nitơ nén bảo quản"),

    (38, "5s", "Wide Shot",
     "Geological 3D cross section model showing underground aquifers and high-pressure water tables surrounding Mount Li mausoleum mound, water seep danger --ar 16:9",
     "Digital water simulation seeping toward subterranean burial chamber walls",
     "[nguy cơ] Hơn thế nữa: mạch nước ngầm khổng lồ dưới chân núi Ly Sơn có thể lập tức nhấn chìm toàn bộ lăng mộ nếu bị chọc thủng.",
     "Tiếng nước ngầm gầm gào cuồn cuộn dưới lòng đất"),

    (39, "5s", "Atmospheric Shot",
     "Ghostly fog of toxic mercury vapor billowing from underground fissure, skull shaped wisp in the vapor, eerie cinematic lighting --ar 16:9",
     "Slow tracking pan through toxic silver mist, light rays piercing through vapor",
     "[cảnh báo nguy hiểm] Và hàng trăm tấn hơi thủy ngân độc hại nén dưới áp suất cao suốt 2.200 năm sẽ phát nổ thành một thảm họa môi trường khủng khiếp!",
     "Tiếng cảnh báo nguy hiểm độc học rền vang"),

    (40, "4s", "Medium Shot",
     "Ancient Chinese bronze crossbow mechanism partially submerged in liquid mercury, still intact and primed to fire, mechanical tension evident --ar 16:9",
     "Slow pan across the primed bronze bowstring still under tension after millennia",
     "[rùng mình] Liệu hệ thống bẫy nỏ tự động ngâm trong thủy ngân không bị rỉ sét vẫn còn hoạt động?",
     "Tiếng dây cung căng cứng rung lên 'Tưng' đầy đe dọa"),

    (41, "5s", "Close-up",
     "Ancient terracotta general statue in full armor, hands folded on bronze sword, silent sentry in darkness, volumetric moonlight beam on face --ar 16:9",
     "Slow cinematic push towards the stone general eyes, shadows shifting",
     "[suy ngẫm] 8.000 chiến binh đất nung ngoài kia thực chất chỉ là những người lính gác cổng ngoại vi.",
     "Âm thanh gió đêm u hoài thổi qua khe hẹp"),

    (42, "4s", "Wide Panoramic",
     "Vast underground military formation of chariots, cavalry horses and kneeling archers ready for war, stretching into darkness --ar 16:9",
     "Sweeping wide angle pan across thousands of ranked terracotta warriors",
     "[nghi vấn lớn] Thứ gì thực sự đang nằm ở trung tâm của hoàng lăng?",
     "Tiếng vó ngựa đá dậm chân trong tưởng tượng"),

    (43, "5s", "Mythological Visual",
     "Mystic ancient map scroll showing the mythical Nine Cauldron vessels of China, celestial dragon seals, ancient seal script calligraphy --ar 16:9",
     "Top-down camera gliding over intricate gold leaf illuminated calligraphy scroll",
     "[bí ẩn cực đại] Cửu Đỉnh - biểu tượng quyền lực tối thượng của nhà Chu bị thất truyền? Hay ngọc tỷ truyền quốc nạm vàng?",
     "Tiếng chuông cổ ngân rung chuyển không gian"),

    (44, "4s", "Dramatic Close-up",
     "Golden Dragon Imperial Seal engraved with Chinese characters 'Thụ Mệnh Vu Thiên, Ký Thọ Vĩnh Xương' resting on red silk pillow --ar 16:9",
     "Slow cinematic reveal of the golden dragon seal glistening with divine authority",
     "[dồn dập] Tất cả những báu vật định đoạt vận mệnh của cả nền văn minh Hoa Hạ có thể đang nằm dưới chân người xem!",
     "Tiếng trống trận giáng một cú nghẹt thở"),

    (45, "5s", "Medium Shot",
     "Ancient terracotta warrior with mysterious etched symbols on back of neck, craftsmen signature names carved 2,200 years ago, forensic macro --ar 16:9",
     "Macro slow tilt over hand-carved ancient seal characters into the back of terracotta neck",
     "[nhân văn] Những người thợ năm xưa đã lén khắc tên mình sau gáy tượng để lại dấu vết của kiếp người nhỏ bé trong công trình khổng lồ.",
     "Tiếng khắc đá lách cách của người thợ cổ"),

    (46, "4s", "Medium Shot",
     "Modern museum visitor standing in front of glass case with illuminated terracotta soldier, reflecting face in glass, past and present merging --ar 16:9",
     "Focus pull from visitor reflection in glass to the ancient warrior eyes inside",
     "[lắng đọng] Khi nhìn vào mắt họ, chúng ta không chỉ nhìn vào đất nung, mà đang nhìn thẳng vào linh hồn của một thời đại hào hùng và đẫm máu.",
     "Âm hưởng vĩ cầm tha thiết da diết"),

    (47, "5s", "Cinematic Wide",
     "Moonlight shining through Mount Li forest, ancient stone mound quiet and untouched under starry galaxy night, peaceful contrast to underground madness --ar 16:9",
     "Slow high angle tilt up from tomb mound to the breathtaking Milky Way galaxy above",
     "[chiêm nghiệm] 2.200 năm trôi qua, các triều đại sụp đổ, các đế chế tan rã... nhưng giấc ngủ của Tần Vương vẫn bất khả xâm phạm.",
     "Tiếng dế đêm kêu thanh bình, tiếng gió đại ngàn rì rào"),

    # Act 4: Scenes 48-55 (Philosophical Conclusion & Viral Call To Action)
    (48, "4s", "Close-up",
     "Golden hourglass with golden sand running out, resting on imperial dragon throne, shadows deepening --ar 16:9",
     "Extreme slow motion macro of golden sand grains falling through glass neck",
     "[chậm rãi triết lý] Kẻ khao khát sống mãi muôn đời rốt cuộc lại giam mình trong chiếc quan tài đồng giữa biển thủy ngân kịch độc.",
     "Tiếng hạt cát rơi khe khẽ vang vọng trong hư vô"),

    (49, "5s", "Medium Shot",
     "Qin Shi Huang in his royal black robe staring out from palace balcony into the sunset of China, wind whipping through banners --ar 16:9",
     "Slow pull back revealing the lonely figure of the emperor against the vast sunset horizon",
     "[thì thầm] Ông đã thống nhất được thiên hạ dưới gầm trời... nhưng không thể thắng nổi quy luật sinh tử của tạo hóa.",
     "Tiếng sáo trúc cổ ai oán ngân dài"),

    (50, "4s", "Dramatic Close-up",
     "Macro shot of terracotta warrior stone face, single tear made of ancient moisture rolling down stone cheek, dramatic cinematic side light --ar 16:9",
     "Ultra slow motion tracking of the water droplet rolling down the weathered cheek",
     "[xúc động] Vĩnh cửu để làm gì khi xung quanh chỉ còn lại bóng tối và đá lạnh nghìn năm?",
     "Nốt nhạc piano trầm mặc ngân vang cô độc"),

    (51, "4s", "Wide Shot",
     "Scientific research station at night outside Xian terracotta museum, radar domes glowing cyan against dark mountains, scientists monitoring screens --ar 16:9",
     "Sleek pan across high-tech telemetry antennae aiming toward the subterranean tomb",
     "[hướng tương lai] Các nhà khoa học quốc tế dự đoán: Có lẽ phải mất thêm từ 30 đến 50 năm nữa...",
     "Tiếng tín hiệu vệ tinh bíp đều đặn"),

    (52, "4s", "Futuristic Vision",
     "Futuristic nano-drones and robotic micro-cameras flying non-invasively through sealed stone chamber cracks, sending 4K holographic scans outside --ar 16:9",
     "Point of view flying through tiny rock crevice, emerging into illuminated golden hall",
     "[kỳ vọng] ...khi công nghệ robot nano và quét không gian 3 chiều hoàn thiện, cánh cửa lăng mộ mới có thể an toàn mở ra.",
     "Âm thanh vù vù công nghệ cao lướt qua không trung"),

    (53, "5s", "Epic Montage",
     "Rapid dynamic montage: Crossbow triggers, swirling silver mercury rivers, 8000 warriors, Emperor golden crown, lightning over Mount Li --ar 16:9",
     "Fast rhythmic camera whip pans between the most breathtaking elements of the tomb",
     "[dồn dập kích thích] Cho đến ngày đó, lăng mộ Tần Thủy Hoàng vẫn sẽ mãi là bí ẩn vĩ đại và đầy khiêu khích nhất hành tinh!",
     "Dàn nhạc giao hưởng bùng nổ cao trào nghẹt thở"),

    (54, "4s", "Dramatic Close-up",
     "Final extreme close up of the terracotta commander eyes, ancient stone eye suddenly catches a spark of golden light, mystery unsolved --ar 16:9",
     "Slow cinematic push into the pupil until the screen fades to black, spark lingering",
     "[kêu gọi tò mò] Bạn tin rằng bên trong quan tài là thi hài nguyên vẹn, hay lăng mộ này vốn dĩ là một cái bẫy khổng lồ?",
     "Cú 'ĐÙNG' bass trầm chấn động rồi tắt lịm trong tĩnh lặng"),

    (55, "4s", "Outro Card",
     "Stylized YouTube cinematic end screen with dark Qin dynasty aesthetic, dragon seal branding, subscribe prompt button in ancient gold font --ar 16:9",
     "Gentle particle floating drift, ambient golden embers rising",
     "[kêu gọi hành động] Hãy để lại bình luận bên dưới, nhấn Đăng ký kênh và bấm Chuông để không bỏ lỡ tập giải mã bí ẩn tiếp theo!",
     "Âm thanh chuông click subscribing thanh thoát vang lên")
]

# Build markdown and structured list
markdown_scenes = []
structured_scenes = []

for item in scene_plans:
    num, timing, camera, img, vid, vo, sfx = item
    raw_block = f"""### [CẢNH {num:02d}] (Thời lượng: {timing} | Góc máy: {camera})
- **Prompt Tạo Ảnh (Midjourney v6 / Flux.1):**
  `{img}`
- **Prompt Chuyển Động (Kling AI / Runway Gen-3 / Luma):**
  `{vid}`
- **Voice-Over (Lời bình):**
  "{vo}"
- **Sound FX & BGM:**
  [{sfx}]
"""
    markdown_scenes.append(raw_block)
    structured_scenes.append({
        "scene_number": num,
        "timing": timing,
        "camera": camera,
        "image_prompt": img,
        "video_prompt": vid,
        "voiceover": vo,
        "sound_fx": sfx,
        "raw_text": raw_block.strip()
    })

full_markdown = f"{part1_outline}\n\n---\n\n# PHẦN 2: CHI TIẾT KỊCH BẢN (55 PROMPT)\n\n" + "\n\n".join(markdown_scenes)

sample_data = {
    "id": "demo",
    "topic": topic,
    "video_type": "Video dài (16:9)",
    "genre": "Bí ẩn / Lịch sử hào hùng",
    "total_scenes": len(structured_scenes),
    "part1_outline": part1_outline,
    "full_markdown": full_markdown,
    "scenes": structured_scenes
}

with open(OUTPUTS_DIR / "script_demo.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f, ensure_ascii=False, indent=2)

with open(OUTPUTS_DIR / "script_demo.md", "w", encoding="utf-8") as f:
    f.write(full_markdown)

print(f"Generated sample demo script with {len(structured_scenes)} scenes successfully!")
