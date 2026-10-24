// AI YouTube Script Director - Frontend Application
document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("file-input");
  const dropPrompt = document.getElementById("drop-prompt");
  const imagePreviewContainer = document.getElementById("image-preview-container");
  const imagePreview = document.getElementById("image-preview");
  const btnRemoveImage = document.getElementById("btn-remove-image");

  const topicInput = document.getElementById("topic-input");
  const sceneCountSlider = document.getElementById("scene-count");
  const sceneCountVal = document.getElementById("scene-count-val");
  const genreSelect = document.getElementById("genre-select");
  const btnGenerate = document.getElementById("btn-generate");
  const btnGenerateText = document.getElementById("btn-generate-text");

  const progressContainer = document.getElementById("progress-container");
  const progressBar = document.getElementById("progress-bar");
  const progressPercent = document.getElementById("progress-percent");
  const progressStatusText = document.getElementById("progress-status-text");

  const outlineContent = document.getElementById("outline-content");
  const outlineEmpty = document.getElementById("outline-empty");
  const scenesContainer = document.getElementById("scenes-container");
  const scenesCountDisplay = document.getElementById("scenes-count-display");
  const scenesBadge = document.getElementById("scenes-badge");
  const scenesFilter = document.getElementById("scenes-filter");

  const fullScriptText = document.getElementById("full-script-text");
  const bulkMjText = document.getElementById("bulk-mj-text");
  const bulkVideoText = document.getElementById("bulk-video-text");
  const bulkVoText = document.getElementById("bulk-vo-text");

  const btnExportCsv = document.getElementById("btn-export-csv");
  const btnCopyAll = document.getElementById("btn-copy-all");
  const btnDownloadMd = document.getElementById("btn-download-md");

  // Settings & History Modals
  const btnOpenSettings = document.getElementById("btn-open-settings");
  const btnCloseSettings = document.getElementById("btn-close-settings");
  const btnCancelSettings = document.getElementById("btn-cancel-settings");
  const btnSaveSettings = document.getElementById("btn-save-settings");
  const settingsModal = document.getElementById("settings-modal");
  const modalProvider = document.getElementById("modal-provider");
  const modalOpenaiKey = document.getElementById("modal-openai-key");
  const modalGeminiKey = document.getElementById("modal-gemini-key");
  const modalOpenaiStatus = document.getElementById("modal-openai-status");
  const modalGeminiStatus = document.getElementById("modal-gemini-status");
  const apiStatusText = document.getElementById("api-status-text");
  const apiStatusDot = document.getElementById("api-status-dot");

  const btnOpenHistory = document.getElementById("btn-open-history");
  const btnCloseHistory = document.getElementById("btn-close-history");
  const historyModal = document.getElementById("history-modal");
  const historyList = document.getElementById("history-list");

  const btnLoadDemo = document.getElementById("btn-load-demo");
  const btnLoadDemoInline = document.getElementById("btn-load-demo-inline");

  // State
  let currentFile = null;
  let selectedVideoType = "Video dài (16:9)";
  let currentScriptData = null;

  // Initialize
  checkApiConfig();

  async function loadDemoScript() {
    try {
      showToast("Đang tải kịch bản mẫu 55 cảnh...");
      const res = await fetch("/api/history/demo");
      if (res.ok) {
        const data = await res.json();
        renderScriptResult(data);
        topicInput.value = data.topic;
        showToast("Đã tải kịch bản mẫu 55 cảnh chuẩn Rule.txt!");
      }
    } catch (e) {
      showToast("Lỗi khi tải kịch bản mẫu", true);
    }
  }

  if (btnLoadDemo) btnLoadDemo.addEventListener("click", loadDemoScript);
  if (btnLoadDemoInline) btnLoadDemoInline.addEventListener("click", loadDemoScript);

  // Video Type Buttons
  document.querySelectorAll(".video-type-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".video-type-btn").forEach((b) => {
        b.classList.remove("active", "border-indigo-500", "bg-indigo-500/10", "text-indigo-300");
        b.classList.add("border-slate-700", "bg-slate-950", "text-slate-400");
      });
      btn.classList.add("active", "border-indigo-500", "bg-indigo-500/10", "text-indigo-300");
      btn.classList.remove("border-slate-700", "bg-slate-950", "text-slate-400");
      selectedVideoType = btn.getAttribute("data-video-type");
    });
  });

  // Slider change
  sceneCountSlider.addEventListener("input", (e) => {
    sceneCountVal.textContent = `${e.target.value} cảnh`;
  });

  // File Upload Handlers
  dropZone.addEventListener("click", (e) => {
    if (e.target !== btnRemoveImage && !btnRemoveImage.contains(e.target)) {
      fileInput.click();
    }
  });

  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      handleImageSelected(e.target.files[0]);
    }
  });

  dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("border-indigo-500", "bg-indigo-500/5");
  });

  dropZone.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dropZone.classList.remove("border-indigo-500", "bg-indigo-500/5");
  });

  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("border-indigo-500", "bg-indigo-500/5");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleImageSelected(e.dataTransfer.files[0]);
    }
  });

  btnRemoveImage.addEventListener("click", (e) => {
    e.stopPropagation();
    currentFile = null;
    fileInput.value = "";
    imagePreview.src = "";
    imagePreviewContainer.classList.add("hidden");
    dropPrompt.classList.remove("hidden");
  });

  function handleImageSelected(file) {
    if (!file.type.startsWith("image/")) {
      showToast("Vui lòng chọn file hình ảnh (JPG, PNG, WEBP)!", true);
      return;
    }
    currentFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.src = e.target.result;
      dropPrompt.classList.add("hidden");
      imagePreviewContainer.classList.remove("hidden");
    };
    reader.readAsDataURL(file);
  }

  // Tabs navigation
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const targetId = btn.getAttribute("data-tab");
      document.querySelectorAll(".tab-btn").forEach((b) => {
        b.classList.remove("active", "text-indigo-400", "bg-indigo-500/10", "border", "border-indigo-500/20");
        b.classList.add("text-slate-400");
      });
      btn.classList.add("active", "text-indigo-400", "bg-indigo-500/10", "border", "border-indigo-500/20");
      btn.classList.remove("text-slate-400");

      document.querySelectorAll(".tab-pane").forEach((pane) => {
        pane.classList.add("hidden");
      });
      const activePane = document.getElementById(targetId);
      if (activePane) activePane.classList.remove("hidden");
    });
  });

  // Scene search/filter
  scenesFilter.addEventListener("input", (e) => {
    const term = e.target.value.toLowerCase();
    const cards = scenesContainer.querySelectorAll(".scene-card");
    cards.forEach((card) => {
      const text = card.textContent.toLowerCase();
      card.style.display = text.includes(term) ? "block" : "none";
    });
  });

  // GENERATE SCRIPT TRIGGER
  btnGenerate.addEventListener("click", async () => {
    const topic = topicInput.value.trim();
    if (!topic && !currentFile) {
      showToast("Vui lòng nhập chủ đề kịch bản hoặc tải lên bức ảnh!", true);
      topicInput.focus();
      return;
    }

    const totalScenes = parseInt(sceneCountSlider.value, 10);
    const genre = genreSelect.value;

    // Start UI progress
    setGeneratingState(true);
    updateProgress(5, "Đang gửi yêu cầu và chuẩn bị pipeline...");

    const formData = new FormData();
    formData.append("topic", topic || "Phân tích bức ảnh và sáng tác kịch bản YouTube đỉnh cao");
    formData.append("video_type", selectedVideoType);
    formData.append("genre", genre);
    formData.append("total_scenes", totalScenes);
    if (currentFile) {
      formData.append("image", currentFile);
    }

    try {
      const response = await fetch("/api/generate-stream", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Lỗi máy chủ: ${response.status}`);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      let buffer = "";

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n\n");
        buffer = lines.pop(); // keep last incomplete chunk

        for (const line of lines) {
          if (line.startsWith("data: ")) {
            const jsonStr = line.slice(6).trim();
            if (jsonStr) {
              const event = JSON.parse(jsonStr);
              if (event.type === "progress") {
                updateProgress(event.percent, event.message);
              } else if (event.type === "complete") {
                updateProgress(100, "Hoàn tất kịch bản!");
                renderScriptResult(event.data);
                showToast("Tạo kịch bản thành công!");
                setTimeout(() => {
                  progressContainer.classList.add("hidden");
                }, 2000);
              } else if (event.type === "error") {
                showToast(`Lỗi: ${event.message}`, true);
                alert(`Đã xảy ra lỗi: ${event.message}`);
              }
            }
          }
        }
      }
    } catch (err) {
      console.error(err);
      showToast(`Lỗi kết nối: ${err.message}`, true);
    } finally {
      setGeneratingState(false);
    }
  });

  function setGeneratingState(isGenerating) {
    btnGenerate.disabled = isGenerating;
    if (isGenerating) {
      btnGenerateText.textContent = "Đang đạo diễn kịch bản...";
      btnGenerate.classList.add("opacity-70", "cursor-not-allowed");
      progressContainer.classList.remove("hidden");
    } else {
      btnGenerateText.textContent = "Tạo Kịch Bản Chuẩn 50-60 Prompt";
      btnGenerate.classList.remove("opacity-70", "cursor-not-allowed");
    }
  }

  function updateProgress(percent, message) {
    progressBar.style.width = `${percent}%`;
    progressPercent.textContent = `${percent}%`;
    progressStatusText.innerHTML = `
      <i class="fa-solid fa-circle-notch fa-spin text-indigo-400"></i>
      <span>${message}</span>
    `;
  }

  // RENDER SCRIPT RESULTS
  function renderScriptResult(data) {
    currentScriptData = data;
    const { part1_outline, full_markdown, scenes } = data;

    // Render Tab 1: Outline
    outlineEmpty.classList.add("hidden");
    outlineContent.classList.remove("hidden");
    if (window.marked) {
      outlineContent.innerHTML = marked.parse(part1_outline);
    } else {
      outlineContent.textContent = part1_outline;
    }

    // Render Tab 2: Scenes Cards
    scenesBadge.textContent = scenes.length;
    scenesCountDisplay.textContent = scenes.length;
    renderSceneCards(scenes);

    // Render Tab 3: Full Markdown
    fullScriptText.value = full_markdown;

    // Render Tab 4: Bulk Export Texts
    const mjPrompts = scenes
      .map((s) => s.image_prompt)
      .filter(Boolean)
      .join("\n\n");
    bulkMjText.value = mjPrompts;

    const vidPrompts = scenes
      .map((s) => `[Cảnh ${s.scene_number}] ${s.video_prompt}`)
      .filter(Boolean)
      .join("\n\n");
    bulkVideoText.value = vidPrompts;

    const voScripts = scenes
      .map((s) => `[Cảnh ${s.scene_number} - ${s.timing}] ${s.voiceover}`)
      .filter(Boolean)
      .join("\n\n");
    bulkVoText.value = voScripts;
  }

  function renderSceneCards(scenes) {
    scenesContainer.innerHTML = "";
    if (!scenes || scenes.length === 0) {
      scenesContainer.innerHTML = `
        <div class="text-center py-16 text-slate-400">
          <p>Không có cảnh nào được tách.</p>
        </div>
      `;
      return;
    }

    scenes.forEach((s) => {
      const card = document.createElement("div");
      card.className = "scene-card bg-slate-950/70 border border-slate-800 rounded-xl p-4 space-y-3.5";
      
      card.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 pb-2.5 border-b border-slate-800/80">
          <div class="flex items-center space-x-2">
            <span class="px-2.5 py-1 rounded-md bg-indigo-600 text-white font-bold text-xs shadow-sm">
              CẢNH ${s.scene_number < 10 ? '0' + s.scene_number : s.scene_number}
            </span>
            <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 text-[11px] border border-slate-700">
              <i class="fa-regular fa-clock text-indigo-400 mr-1"></i>${s.timing}
            </span>
            <span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300 text-[11px] border border-slate-700">
              <i class="fa-solid fa-video text-cyan-400 mr-1"></i>${s.camera}
            </span>
          </div>

          <div class="flex items-center space-x-1.5">
            <button onclick="copyToClipboard('${escapeHtml(s.image_prompt)}', 'Prompt Ảnh')" title="Copy Prompt Midjourney" 
              class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-emerald-400 text-xs border border-slate-700 transition flex items-center space-x-1">
              <i class="fa-regular fa-image"></i>
              <span>Copy Ảnh</span>
            </button>
            <button onclick="copyToClipboard('${escapeHtml(s.video_prompt)}', 'Prompt Video')" title="Copy Prompt Motion Video" 
              class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-cyan-400 text-xs border border-slate-700 transition flex items-center space-x-1">
              <i class="fa-solid fa-film"></i>
              <span>Copy Video</span>
            </button>
            <button onclick="copyToClipboard('${escapeHtml(s.voiceover)}', 'Voice-Over')" title="Copy Lời Bình" 
              class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-pink-400 text-xs border border-slate-700 transition flex items-center space-x-1">
              <i class="fa-solid fa-microphone"></i>
              <span>Copy Voice</span>
            </button>
          </div>
        </div>

        <!-- Image Prompt -->
        <div class="space-y-1">
          <div class="text-[11px] font-semibold text-emerald-400 uppercase tracking-wider flex items-center space-x-1">
            <i class="fa-solid fa-palette text-xs"></i>
            <span>Prompt Tạo Ảnh (Midjourney v6 / Flux.1):</span>
          </div>
          <div class="bg-slate-900 border border-slate-800/90 rounded-lg p-2.5 font-mono text-xs text-slate-200 select-all leading-relaxed">
            ${escapeHtml(s.image_prompt || "Chưa có prompt ảnh")}
          </div>
        </div>

        <!-- Video Motion Prompt -->
        <div class="space-y-1">
          <div class="text-[11px] font-semibold text-cyan-400 uppercase tracking-wider flex items-center space-x-1">
            <i class="fa-solid fa-camera-rotate text-xs"></i>
            <span>Prompt Chuyển Động Video (Kling AI / Runway Gen-3 / Luma):</span>
          </div>
          <div class="bg-slate-900 border border-slate-800/90 rounded-lg p-2 font-mono text-xs text-slate-300 select-all">
            ${escapeHtml(s.video_prompt || "Chưa có prompt video")}
          </div>
        </div>

        <!-- Voice-Over -->
        <div class="space-y-1">
          <div class="text-[11px] font-semibold text-pink-400 uppercase tracking-wider flex items-center space-x-1">
            <i class="fa-solid fa-volume-high text-xs"></i>
            <span>Voice-Over (Lời bình & Ngữ điệu):</span>
          </div>
          <div class="bg-slate-900 border border-slate-800/90 rounded-lg p-2.5 text-xs text-slate-200 leading-relaxed italic">
            "${escapeHtml(s.voiceover || "Chưa có lời bình")}"
          </div>
        </div>

        ${s.sound_fx ? `
        <!-- Sound FX -->
        <div class="text-[11px] text-amber-300/90 bg-amber-500/10 border border-amber-500/20 px-2.5 py-1.5 rounded-lg flex items-center space-x-2">
          <i class="fa-solid fa-bolt-lightning text-amber-400"></i>
          <span><strong>Sound FX:</strong> ${escapeHtml(s.sound_fx)}</span>
        </div>
        ` : ''}
      `;
      scenesContainer.appendChild(card);
    });
  }

  // Export CSV
  btnExportCsv.addEventListener("click", async () => {
    if (!currentScriptData || !currentScriptData.scenes || currentScriptData.scenes.length === 0) {
      showToast("Chưa có kịch bản để xuất CSV!", true);
      return;
    }

    try {
      const response = await fetch("/api/export-csv", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ scenes: currentScriptData.scenes }),
      });
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `kich_ban_${currentScriptData.topic.slice(0, 20)}.csv`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      showToast("Đã tải xuống file CSV!");
    } catch (err) {
      showToast("Lỗi khi tải file CSV", true);
    }
  });

  // Download Markdown file
  btnDownloadMd.addEventListener("click", () => {
    if (!fullScriptText.value) {
      showToast("Chưa có nội dung để tải!", true);
      return;
    }
    const blob = new Blob([fullScriptText.value], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "kich_ban_ai_full.md";
    document.body.appendChild(a);
    a.click();
    a.remove();
    showToast("Đã tải file Markdown!");
  });

  // Copy All button
  btnCopyAll.addEventListener("click", () => {
    if (!fullScriptText.value) {
      showToast("Chưa có nội dung kịch bản để copy!", true);
      return;
    }
    navigator.clipboard.writeText(fullScriptText.value);
    showToast("Đã sao chép toàn bộ kịch bản vào Clipboard!");
  });

  // API Config checking & settings modal
  const quickGeminiKey = document.getElementById("quick-gemini-key");
  const btnSaveQuickGemini = document.getElementById("btn-save-quick-gemini");
  const geminiBannerStatus = document.getElementById("gemini-banner-status");

  async function checkApiConfig() {
    try {
      const res = await fetch("/api/config");
      const data = await res.json();
      modalProvider.value = data.provider;
      modalOpenaiStatus.textContent = `Hiện tại: ${data.openai_masked}`;
      modalGeminiStatus.textContent = `Hiện tại: ${data.gemini_masked}`;

      if (data.provider === "gemini") {
        if (data.has_gemini) {
          apiStatusDot.className = "w-2 h-2 rounded-full bg-emerald-400";
          apiStatusText.textContent = "Google Gemini (Miễn phí) Sẵn Sàng";
          if (geminiBannerStatus) geminiBannerStatus.classList.remove("hidden");
          if (quickGeminiKey) quickGeminiKey.placeholder = `Đã lưu key: ${data.gemini_masked}`;
        } else {
          apiStatusDot.className = "w-2 h-2 rounded-full bg-amber-400 animate-pulse";
          apiStatusText.textContent = "Google Gemini: Cần nhập API Key";
          if (geminiBannerStatus) geminiBannerStatus.classList.add("hidden");
        }
      } else if (data.provider === "openai" && data.has_openai) {
        apiStatusDot.className = "w-2 h-2 rounded-full bg-emerald-400";
        apiStatusText.textContent = "OpenAI (GPT-4o) Sẵn Sàng";
      } else {
        apiStatusDot.className = "w-2 h-2 rounded-full bg-red-400";
        apiStatusText.textContent = "Chưa có API Key";
      }
    } catch (e) {
      apiStatusDot.className = "w-2 h-2 rounded-full bg-red-400";
      apiStatusText.textContent = "Lỗi kết nối API";
    }
  }

  async function saveGeminiKey(key) {
    if (!key) {
      showToast("Vui lòng dán Google Gemini API Key!", true);
      return;
    }
    try {
      const res = await fetch("/api/config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          provider: "gemini",
          gemini_key: key
        }),
      });
      if (res.ok) {
        showToast("Đã kích hoạt Google Gemini miễn phí thành công!");
        quickGeminiKey.value = "";
        checkApiConfig();
      }
    } catch (e) {
      showToast("Lỗi khi lưu key", true);
    }
  }

  if (btnSaveQuickGemini) {
    btnSaveQuickGemini.addEventListener("click", () => {
      saveGeminiKey(quickGeminiKey.value.trim());
    });
  }

  if (quickGeminiKey) {
    quickGeminiKey.addEventListener("keydown", (e) => {
      if (e.key === "Enter") {
        saveGeminiKey(quickGeminiKey.value.trim());
      }
    });
  }

  btnOpenSettings.addEventListener("click", () => {
    settingsModal.classList.remove("hidden");
  });
  btnCloseSettings.addEventListener("click", () => settingsModal.classList.add("hidden"));
  btnCancelSettings.addEventListener("click", () => settingsModal.classList.add("hidden"));

  btnSaveSettings.addEventListener("click", async () => {
    const payload = {
      provider: modalProvider.value,
    };
    if (modalOpenaiKey.value.trim()) payload.openai_key = modalOpenaiKey.value.trim();
    if (modalGeminiKey.value.trim()) payload.gemini_key = modalGeminiKey.value.trim();

    try {
      const res = await fetch("/api/config", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (res.ok) {
        showToast("Đã lưu cấu hình API!");
        settingsModal.classList.add("hidden");
        checkApiConfig();
      }
    } catch (e) {
      showToast("Lỗi lưu cấu hình", true);
    }
  });

  // History modal
  btnOpenHistory.addEventListener("click", async () => {
    historyModal.classList.remove("hidden");
    historyList.innerHTML = `<div class="text-center py-6 text-slate-400">Đang tải lịch sử...</div>`;
    try {
      const res = await fetch("/api/history");
      const list = await res.json();
      if (!list || list.length === 0) {
        historyList.innerHTML = `<div class="text-center py-8 text-slate-400">Chưa có kịch bản nào được lưu trong thư mục outputs.</div>`;
        return;
      }
      historyList.innerHTML = "";
      list.forEach((item) => {
        const row = document.createElement("div");
        row.className = "flex items-center justify-between p-3 rounded-xl bg-slate-950 hover:bg-slate-800/80 border border-slate-800 cursor-pointer transition";
        row.innerHTML = `
          <div>
            <h4 class="font-semibold text-xs text-slate-200 line-clamp-1">${escapeHtml(item.topic)}</h4>
            <p class="text-[10px] text-slate-400 mt-0.5">${item.scenes_count} cảnh • ${escapeHtml(item.video_type)} • ${escapeHtml(item.genre)}</p>
          </div>
          <button class="px-2.5 py-1 text-xs bg-indigo-600/30 text-indigo-300 hover:bg-indigo-600 hover:text-white rounded-lg transition">Mở</button>
        `;
        row.addEventListener("click", async () => {
          try {
            const detailRes = await fetch(`/api/history/${item.id}`);
            const scriptData = await detailRes.json();
            renderScriptResult(scriptData);
            historyModal.classList.add("hidden");
            showToast(`Đã mở kịch bản: ${item.topic.slice(0, 25)}...`);
          } catch (e) {
            showToast("Lỗi khi mở kịch bản", true);
          }
        });
        historyList.appendChild(row);
      });
    } catch (e) {
      historyList.innerHTML = `<div class="text-center py-6 text-red-400">Không thể tải lịch sử</div>`;
    }
  });

  // Import Modal (Gemini Argon Direct Paste)
  const btnOpenImport = document.getElementById("btn-open-import");
  const btnCloseImport = document.getElementById("btn-close-import");
  const btnCancelImport = document.getElementById("btn-cancel-import");
  const btnSubmitImport = document.getElementById("btn-submit-import");
  const importModal = document.getElementById("import-modal");
  const importTopic = document.getElementById("import-topic");
  const importText = document.getElementById("import-text");

  if (btnOpenImport) {
    btnOpenImport.addEventListener("click", () => {
      importModal.classList.remove("hidden");
      importText.focus();
    });
  }
  if (btnCloseImport) btnCloseImport.addEventListener("click", () => importModal.classList.add("hidden"));
  if (btnCancelImport) btnCancelImport.addEventListener("click", () => importModal.classList.add("hidden"));

  if (btnSubmitImport) {
    btnSubmitImport.addEventListener("click", async () => {
      const text = importText.value.trim();
      if (!text) {
        showToast("Vui lòng dán nội dung kịch bản!", true);
        return;
      }
      const topic = importTopic.value.trim() || "Kịch bản tạo bởi Gemini Argon";

      try {
        btnSubmitImport.disabled = true;
        btnSubmitImport.textContent = "Đang xử lý...";
        const res = await fetch("/api/parse-and-save", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            text: text,
            topic: topic,
            video_type: selectedVideoType,
            genre: genreSelect.value
          }),
        });

        if (!res.ok) {
          throw new Error("Không thể xử lý kịch bản");
        }

        const data = await res.json();
        renderScriptResult(data);
        topicInput.value = data.topic;
        importModal.classList.add("hidden");
        importText.value = "";
        importTopic.value = "";
        showToast(`Đã tách thành công ${data.total_scenes} cảnh kịch bản!`);

        // Switch to scenes tab
        const scenesTabBtn = document.querySelector('[data-tab="tab-scenes"]');
        if (scenesTabBtn) scenesTabBtn.click();
      } catch (e) {
        showToast(e.message || "Lỗi xử lý kịch bản", true);
      } finally {
        btnSubmitImport.disabled = false;
        btnSubmitImport.textContent = "Xử Lý & Tách Thẻ Phân Cảnh Ngay";
      }
    });
  }

  btnCloseHistory.addEventListener("click", () => historyModal.classList.add("hidden"));
});

// Global helpers
function showToast(message, isError = false) {
  const toast = document.getElementById("toast");
  const msgEl = document.getElementById("toast-message");
  if (!toast) return;

  msgEl.textContent = message;
  toast.className = `fixed bottom-5 right-5 px-4 py-2.5 rounded-xl shadow-2xl text-xs font-medium flex items-center space-x-2 transform transition-all duration-300 z-50 ${
    isError ? "bg-red-600 text-white" : "bg-indigo-600 text-white"
  }`;
  toast.classList.remove("translate-y-20", "opacity-0");

  setTimeout(() => {
    toast.classList.add("translate-y-20", "opacity-0");
  }, 2500);
}

function copyToClipboard(text, label = "Nội dung") {
  if (!text) return;
  navigator.clipboard.writeText(text);
  showToast(`Đã copy ${label}!`);
}

function copyElementText(elementId) {
  const el = document.getElementById(elementId);
  if (!el || !el.value) return;
  navigator.clipboard.writeText(el.value);
  showToast("Đã copy danh sách prompt vào Clipboard!");
}

function escapeHtml(text) {
  if (!text) return "";
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
