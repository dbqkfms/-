/**
 * Seedream 4.5 - AI Image Generator
 * Client-side JavaScript
 */

// ============================================================
// Configuration & State
// ============================================================

const CONFIG = {
    API_PROVIDERS: {
        aimlapi: {
            url: 'https://api.aimlapi.com/v1/images/generations',
            model: 'bytedance/seedream-4-5'
        },
        byteplus: {
            url: 'https://api.byteplus.com/v1/images/generations',
            model: 'doubao-seedream-4-5-251128'
        }
    },
    MAX_FILE_SIZE: 10 * 1024 * 1024, // 10MB
    ALLOWED_TYPES: ['image/jpeg', 'image/png', 'image/gif', 'image/webp'],
    MAX_SLOTS: 5
};

const state = {
    mode: 'text2img', // text2img, img2img, parallel
    apiKey: '',
    provider: 'aimlapi',
    maxConcurrent: 5,
    saveHistory: true,
    isGenerating: false,
    referenceImages: {}, // { slot: { file: File, dataUrl: string } }
    results: [],
    history: []
};

// ============================================================
// DOM Elements
// ============================================================

const elements = {
    // Mode
    modeBtns: document.querySelectorAll('.mode-btn'),

    // Input
    promptInput: document.getElementById('promptInput'),
    charCount: document.getElementById('charCount'),
    clearPrompt: document.getElementById('clearPrompt'),
    referenceSection: document.getElementById('referenceSection'),
    singleUpload: document.getElementById('singleUpload'),
    singleFileInput: document.getElementById('singleFileInput'),
    parallelSlots: document.getElementById('parallelSlots'),
    previewArea: document.getElementById('previewArea'),
    previewGrid: document.getElementById('previewGrid'),
    slotHint: document.getElementById('slotHint'),

    // Options
    imageSize: document.getElementById('imageSize'),
    imageCount: document.getElementById('imageCount'),
    seedInput: document.getElementById('seedInput'),
    watermarkCheck: document.getElementById('watermarkCheck'),

    // Generate
    generateBtn: document.getElementById('generateBtn'),

    // Progress
    progressSection: document.getElementById('progressSection'),
    progressFill: document.getElementById('progressFill'),
    progressText: document.getElementById('progressText'),
    progressPercent: document.getElementById('progressPercent'),
    parallelProgress: document.getElementById('parallelProgress'),

    // Results
    resultsArea: document.getElementById('resultsArea'),
    emptyState: document.getElementById('emptyState'),
    resultsGrid: document.getElementById('resultsGrid'),
    downloadAllBtn: document.getElementById('downloadAllBtn'),
    clearResultsBtn: document.getElementById('clearResultsBtn'),

    // History
    historyToggle: document.getElementById('historyToggle'),
    historyCount: document.getElementById('historyCount'),

    // Modals
    settingsModal: document.getElementById('settingsModal'),
    settingsBtn: document.getElementById('settingsBtn'),
    closeSettings: document.getElementById('closeSettings'),
    cancelSettings: document.getElementById('cancelSettings'),
    saveSettings: document.getElementById('saveSettings'),
    apiKeyInput: document.getElementById('apiKeyInput'),
    toggleApiKey: document.getElementById('toggleApiKey'),
    apiProvider: document.getElementById('apiProvider'),
    maxConcurrent: document.getElementById('maxConcurrent'),
    saveHistoryCheck: document.getElementById('saveHistory'),

    imageModal: document.getElementById('imageModal'),
    modalImage: document.getElementById('modalImage'),
    closeImageModal: document.getElementById('closeImageModal'),
    downloadImage: document.getElementById('downloadImage'),
    copyImage: document.getElementById('copyImage'),
    useAsReference: document.getElementById('useAsReference'),

    historyModal: document.getElementById('historyModal'),
    closeHistory: document.getElementById('closeHistory'),
    clearHistory: document.getElementById('clearHistory'),
    historyList: document.getElementById('historyList'),

    // Toast
    toastContainer: document.getElementById('toastContainer')
};

// ============================================================
// Initialization
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    loadSettings();
    loadHistory();
    initEventListeners();
    initParallelSlots();
    updateUI();
});

function loadSettings() {
    const saved = localStorage.getItem('seedream_settings');
    if (saved) {
        const settings = JSON.parse(saved);
        state.apiKey = settings.apiKey || '';
        state.provider = settings.provider || 'aimlapi';
        state.maxConcurrent = settings.maxConcurrent || 5;
        state.saveHistory = settings.saveHistory !== false;
    }
}

function saveSettings() {
    localStorage.setItem('seedream_settings', JSON.stringify({
        apiKey: state.apiKey,
        provider: state.provider,
        maxConcurrent: state.maxConcurrent,
        saveHistory: state.saveHistory
    }));
}

function loadHistory() {
    const saved = localStorage.getItem('seedream_history');
    if (saved) {
        state.history = JSON.parse(saved);
        updateHistoryCount();
    }
}

function saveHistory() {
    if (state.saveHistory) {
        // Keep only last 50 items
        const toSave = state.history.slice(-50);
        localStorage.setItem('seedream_history', JSON.stringify(toSave));
    }
}

// ============================================================
// Event Listeners
// ============================================================

function initEventListeners() {
    // Mode selection
    elements.modeBtns.forEach(btn => {
        btn.addEventListener('click', () => setMode(btn.dataset.mode));
    });

    // Prompt
    elements.promptInput.addEventListener('input', updateCharCount);
    elements.clearPrompt.addEventListener('click', () => {
        elements.promptInput.value = '';
        updateCharCount();
    });

    // Single file upload
    elements.singleUpload.addEventListener('click', () => elements.singleFileInput.click());
    elements.singleFileInput.addEventListener('change', handleSingleFileSelect);

    // Drag and drop for single upload
    elements.singleUpload.addEventListener('dragover', handleDragOver);
    elements.singleUpload.addEventListener('dragleave', handleDragLeave);
    elements.singleUpload.addEventListener('drop', handleSingleDrop);

    // Generate
    elements.generateBtn.addEventListener('click', generate);

    // Results actions
    elements.downloadAllBtn.addEventListener('click', downloadAll);
    elements.clearResultsBtn.addEventListener('click', clearResults);

    // Settings modal
    elements.settingsBtn.addEventListener('click', openSettings);
    elements.closeSettings.addEventListener('click', closeSettings);
    elements.cancelSettings.addEventListener('click', closeSettings);
    elements.saveSettings.addEventListener('click', handleSaveSettings);
    elements.toggleApiKey.addEventListener('click', toggleApiKeyVisibility);

    // Image modal
    elements.closeImageModal.addEventListener('click', closeImageModal);
    elements.downloadImage.addEventListener('click', downloadCurrentImage);
    elements.copyImage.addEventListener('click', copyCurrentImage);
    elements.useAsReference.addEventListener('click', useCurrentAsReference);

    // History
    elements.historyToggle.addEventListener('click', openHistory);
    elements.closeHistory.addEventListener('click', closeHistory);
    elements.clearHistory.addEventListener('click', handleClearHistory);

    // Modal backdrop clicks
    document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
        backdrop.addEventListener('click', () => {
            closeSettings();
            closeImageModal();
            closeHistory();
        });
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', handleKeydown);
}

function initParallelSlots() {
    elements.parallelSlots.innerHTML = '';

    for (let i = 1; i <= CONFIG.MAX_SLOTS; i++) {
        const slot = document.createElement('div');
        slot.className = 'slot-item';
        slot.dataset.slot = i;
        slot.innerHTML = `
            <span class="slot-number">Slot ${i}</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="5" x2="12" y2="19"/>
                <line x1="5" y1="12" x2="19" y2="12"/>
            </svg>
            <input type="file" accept="image/*" hidden>
        `;

        const input = slot.querySelector('input');

        slot.addEventListener('click', (e) => {
            if (!e.target.closest('.slot-remove')) {
                input.click();
            }
        });

        input.addEventListener('change', (e) => handleSlotFileSelect(e, i));

        slot.addEventListener('dragover', handleDragOver);
        slot.addEventListener('dragleave', handleDragLeave);
        slot.addEventListener('drop', (e) => handleSlotDrop(e, i));

        elements.parallelSlots.appendChild(slot);
    }
}

// ============================================================
// Mode Management
// ============================================================

function setMode(mode) {
    state.mode = mode;

    elements.modeBtns.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.mode === mode);
    });

    updateUI();
}

function updateUI() {
    const showReference = state.mode !== 'text2img';
    const showParallel = state.mode === 'parallel';

    elements.referenceSection.style.display = showReference ? 'block' : 'none';
    elements.singleUpload.style.display = showParallel ? 'none' : 'block';
    elements.parallelSlots.style.display = showParallel ? 'grid' : 'none';
    elements.slotHint.textContent = showParallel ? '최대 5개 슬롯' : '1개 이미지';

    // Update generate button text
    const btnText = elements.generateBtn.querySelector('span');
    if (state.mode === 'text2img') {
        btnText.textContent = '이미지 생성';
    } else if (state.mode === 'img2img') {
        btnText.textContent = '이미지 편집';
    } else {
        btnText.textContent = '병렬 처리';
    }
}

// ============================================================
// File Handling
// ============================================================

function handleDragOver(e) {
    e.preventDefault();
    e.currentTarget.classList.add('dragover');
}

function handleDragLeave(e) {
    e.currentTarget.classList.remove('dragover');
}

function handleSingleFileSelect(e) {
    const file = e.target.files[0];
    if (file) {
        processFile(file, 1);
    }
}

function handleSingleDrop(e) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    if (file) {
        processFile(file, 1);
    }
}

function handleSlotFileSelect(e, slot) {
    const file = e.target.files[0];
    if (file) {
        processFile(file, slot);
    }
}

function handleSlotDrop(e, slot) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    if (file) {
        processFile(file, slot);
    }
}

async function processFile(file, slot) {
    // Validate file
    if (!CONFIG.ALLOWED_TYPES.includes(file.type)) {
        showToast('지원하지 않는 파일 형식입니다.', 'error');
        return;
    }

    if (file.size > CONFIG.MAX_FILE_SIZE) {
        showToast('파일 크기는 10MB 이하여야 합니다.', 'error');
        return;
    }

    // Read file
    const dataUrl = await readFileAsDataURL(file);

    // Store
    state.referenceImages[slot] = {
        file,
        dataUrl
    };

    // Update UI
    updateSlotUI(slot, dataUrl);
    updatePreview();
}

function readFileAsDataURL(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(file);
    });
}

function updateSlotUI(slot, dataUrl) {
    if (state.mode === 'parallel') {
        const slotElement = document.querySelector(`.slot-item[data-slot="${slot}"]`);
        if (slotElement) {
            slotElement.classList.add('has-image');
            slotElement.innerHTML = `
                <span class="slot-number">Slot ${slot}</span>
                <img src="${dataUrl}" class="slot-preview" alt="Preview">
                <button class="slot-remove" onclick="removeSlotImage(${slot})">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"/>
                        <line x1="6" y1="6" x2="18" y2="18"/>
                    </svg>
                </button>
                <input type="file" accept="image/*" hidden>
            `;

            const input = slotElement.querySelector('input');
            input.addEventListener('change', (e) => handleSlotFileSelect(e, slot));
        }
    } else {
        // Single upload - show in upload zone
        elements.singleUpload.innerHTML = `
            <img src="${dataUrl}" class="slot-preview" style="width: 100%; height: 200px; object-fit: contain; border-radius: 8px;">
            <button class="slot-remove" onclick="removeSingleImage()" style="opacity: 1;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                </svg>
            </button>
        `;
    }
}

function removeSlotImage(slot) {
    delete state.referenceImages[slot];

    const slotElement = document.querySelector(`.slot-item[data-slot="${slot}"]`);
    if (slotElement) {
        slotElement.classList.remove('has-image');
        slotElement.innerHTML = `
            <span class="slot-number">Slot ${slot}</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="12" y1="5" x2="12" y2="19"/>
                <line x1="5" y1="12" x2="19" y2="12"/>
            </svg>
            <input type="file" accept="image/*" hidden>
        `;

        const input = slotElement.querySelector('input');
        input.addEventListener('change', (e) => handleSlotFileSelect(e, slot));
    }

    updatePreview();
}

window.removeSlotImage = removeSlotImage;

function removeSingleImage() {
    delete state.referenceImages[1];

    elements.singleUpload.innerHTML = `
        <div class="upload-content">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="17,8 12,3 7,8"/>
                <line x1="12" y1="3" x2="12" y2="15"/>
            </svg>
            <p>이미지를 드래그하거나 클릭하여 업로드</p>
            <span class="upload-hint">PNG, JPG, WEBP (최대 10MB)</span>
        </div>
    `;

    updatePreview();
}

window.removeSingleImage = removeSingleImage;

function updatePreview() {
    const images = Object.values(state.referenceImages);

    if (images.length > 0) {
        elements.previewArea.style.display = 'block';
        elements.previewGrid.innerHTML = images.map((img, idx) => `
            <div class="preview-item">
                <img src="${img.dataUrl}" alt="Preview ${idx + 1}">
            </div>
        `).join('');
    } else {
        elements.previewArea.style.display = 'none';
        elements.previewGrid.innerHTML = '';
    }
}

// ============================================================
// Prompt Handling
// ============================================================

function updateCharCount() {
    const count = elements.promptInput.value.length;
    elements.charCount.textContent = count;
}

// ============================================================
// Generation
// ============================================================

async function generate() {
    // Validate
    if (!state.apiKey) {
        showToast('API Key를 설정해주세요.', 'error');
        openSettings();
        return;
    }

    const prompt = elements.promptInput.value.trim();
    if (!prompt) {
        showToast('프롬프트를 입력해주세요.', 'error');
        elements.promptInput.focus();
        return;
    }

    if (state.mode !== 'text2img' && Object.keys(state.referenceImages).length === 0) {
        showToast('참조 이미지를 업로드해주세요.', 'error');
        return;
    }

    // Start generation
    state.isGenerating = true;
    updateGenerateButton(true);
    showProgress();

    try {
        if (state.mode === 'parallel') {
            await generateParallel(prompt);
        } else {
            await generateSingle(prompt);
        }
    } catch (error) {
        console.error('Generation error:', error);
        showToast(`생성 실패: ${error.message}`, 'error');
    } finally {
        state.isGenerating = false;
        updateGenerateButton(false);
        hideProgress();
    }
}

async function generateSingle(prompt) {
    const options = getOptions();
    const referenceImage = state.referenceImages[1]?.dataUrl || null;

    updateProgress(0, '이미지 생성 중...');

    const result = await callAPI({
        prompt,
        referenceImages: referenceImage ? [referenceImage] : null,
        ...options
    });

    if (result.success) {
        updateProgress(100, '완료!');
        addResults(result.data, prompt);
        showToast('이미지 생성 완료!', 'success');
    } else {
        throw new Error(result.error);
    }
}

async function generateParallel(prompt) {
    const options = getOptions();
    const slots = Object.entries(state.referenceImages);

    if (slots.length === 0) {
        throw new Error('참조 이미지가 없습니다.');
    }

    // Show parallel progress
    elements.parallelProgress.style.display = 'block';
    elements.parallelProgress.innerHTML = slots.map(([slot]) => `
        <div class="parallel-item" data-slot="${slot}">
            <span class="parallel-item-slot">Slot ${slot}</span>
            <div class="parallel-item-bar">
                <div class="parallel-item-fill" style="width: 0%"></div>
            </div>
            <span class="parallel-item-status">대기 중</span>
        </div>
    `).join('');

    // Create tasks
    const tasks = slots.map(([slot, img]) => ({
        slot: parseInt(slot),
        referenceImage: img.dataUrl
    }));

    // Process with concurrency limit
    const results = [];
    const concurrency = Math.min(state.maxConcurrent, tasks.length);
    let completed = 0;

    const processTask = async (task) => {
        const slotElement = document.querySelector(`.parallel-item[data-slot="${task.slot}"]`);
        const fillElement = slotElement?.querySelector('.parallel-item-fill');
        const statusElement = slotElement?.querySelector('.parallel-item-status');

        if (statusElement) statusElement.textContent = '처리 중...';
        if (fillElement) fillElement.style.width = '50%';

        try {
            const result = await callAPI({
                prompt,
                referenceImages: [task.referenceImage],
                ...options
            });

            if (result.success) {
                if (fillElement) fillElement.style.width = '100%';
                if (statusElement) statusElement.textContent = '완료';
                if (slotElement) slotElement.classList.add('completed');

                results.push({
                    slot: task.slot,
                    data: result.data
                });
            } else {
                throw new Error(result.error);
            }
        } catch (error) {
            if (fillElement) fillElement.style.width = '100%';
            if (statusElement) statusElement.textContent = '실패';
            if (slotElement) slotElement.classList.add('error');

            results.push({
                slot: task.slot,
                error: error.message
            });
        }

        completed++;
        updateProgress(
            Math.round((completed / tasks.length) * 100),
            `${completed}/${tasks.length} 완료`
        );
    };

    // Process in batches
    for (let i = 0; i < tasks.length; i += concurrency) {
        const batch = tasks.slice(i, i + concurrency);
        await Promise.all(batch.map(processTask));
    }

    // Add successful results
    const successResults = results.filter(r => r.data);
    if (successResults.length > 0) {
        successResults.forEach(r => {
            addResults(r.data, prompt, r.slot);
        });
        showToast(`${successResults.length}개 슬롯 처리 완료!`, 'success');
    }

    const failedCount = results.filter(r => r.error).length;
    if (failedCount > 0) {
        showToast(`${failedCount}개 슬롯 처리 실패`, 'warning');
    }
}

function getOptions() {
    return {
        imageSize: elements.imageSize.value,
        n: parseInt(elements.imageCount.value),
        seed: elements.seedInput.value ? parseInt(elements.seedInput.value) : null,
        watermark: elements.watermarkCheck.checked
    };
}

async function callAPI({ prompt, referenceImages, imageSize, n, seed, watermark }) {
    const config = CONFIG.API_PROVIDERS[state.provider];

    const payload = {
        model: config.model,
        prompt,
        image_size: imageSize,
        n: n || 1,
        response_format: 'url'
    };

    if (referenceImages && referenceImages.length > 0) {
        payload.image_urls = referenceImages;
    }

    if (seed !== null) {
        payload.seed = seed;
    }

    if (watermark) {
        payload.watermark = true;
    }

    try {
        const response = await fetch(config.url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${state.apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (!response.ok) {
            return {
                success: false,
                error: result.error?.message || `API Error: ${response.status}`
            };
        }

        return {
            success: true,
            data: result.data || []
        };
    } catch (error) {
        return {
            success: false,
            error: error.message
        };
    }
}

// ============================================================
// Results
// ============================================================

function addResults(data, prompt, slot = null) {
    const timestamp = new Date().toISOString();

    data.forEach((item, idx) => {
        const result = {
            id: `${Date.now()}_${idx}`,
            url: item.url || item.b64_json,
            isBase64: !!item.b64_json,
            prompt,
            slot,
            timestamp
        };

        state.results.unshift(result);

        // Add to history
        if (state.saveHistory) {
            state.history.push({
                ...result,
                thumbnail: item.url || `data:image/png;base64,${item.b64_json?.substring(0, 100)}`
            });
            saveHistory();
            updateHistoryCount();
        }
    });

    renderResults();
}

function renderResults() {
    if (state.results.length === 0) {
        elements.emptyState.style.display = 'flex';
        elements.resultsGrid.style.display = 'none';
        elements.downloadAllBtn.disabled = true;
        elements.clearResultsBtn.disabled = true;
        return;
    }

    elements.emptyState.style.display = 'none';
    elements.resultsGrid.style.display = 'grid';
    elements.downloadAllBtn.disabled = false;
    elements.clearResultsBtn.disabled = false;

    elements.resultsGrid.innerHTML = state.results.map(result => `
        <div class="result-item" onclick="openImageModal('${result.id}')">
            ${result.slot ? `<span class="result-slot">Slot ${result.slot}</span>` : ''}
            <img src="${result.isBase64 ? `data:image/png;base64,${result.url}` : result.url}" alt="Generated">
            <div class="result-overlay">
                <div class="result-actions">
                    <button class="btn-icon" onclick="event.stopPropagation(); downloadResult('${result.id}')" title="Download">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                            <polyline points="7,10 12,15 17,10"/>
                            <line x1="12" y1="15" x2="12" y2="3"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

function clearResults() {
    state.results = [];
    renderResults();
    showToast('결과가 삭제되었습니다.', 'success');
}

async function downloadResult(id) {
    const result = state.results.find(r => r.id === id);
    if (!result) return;

    try {
        let blob;

        if (result.isBase64) {
            const byteString = atob(result.url);
            const ab = new ArrayBuffer(byteString.length);
            const ia = new Uint8Array(ab);
            for (let i = 0; i < byteString.length; i++) {
                ia[i] = byteString.charCodeAt(i);
            }
            blob = new Blob([ab], { type: 'image/png' });
        } else {
            const response = await fetch(result.url);
            blob = await response.blob();
        }

        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `seedream_${result.id}.png`;
        a.click();
        URL.revokeObjectURL(url);

        showToast('다운로드 완료!', 'success');
    } catch (error) {
        showToast('다운로드 실패', 'error');
    }
}

window.downloadResult = downloadResult;

async function downloadAll() {
    for (const result of state.results) {
        await downloadResult(result.id);
        await new Promise(resolve => setTimeout(resolve, 500));
    }
}

// ============================================================
// Progress UI
// ============================================================

function showProgress() {
    elements.progressSection.style.display = 'block';
    updateProgress(0, '준비 중...');
}

function hideProgress() {
    setTimeout(() => {
        elements.progressSection.style.display = 'none';
        elements.parallelProgress.style.display = 'none';
    }, 1000);
}

function updateProgress(percent, text) {
    elements.progressFill.style.width = `${percent}%`;
    elements.progressText.textContent = text;
    elements.progressPercent.textContent = `${percent}%`;
}

function updateGenerateButton(loading) {
    const btn = elements.generateBtn;
    const span = btn.querySelector('span');

    if (loading) {
        btn.classList.add('loading');
        btn.disabled = true;
        span.textContent = '생성 중...';
    } else {
        btn.classList.remove('loading');
        btn.disabled = false;
        updateUI(); // Reset button text based on mode
    }
}

// ============================================================
// Settings Modal
// ============================================================

function openSettings() {
    elements.settingsModal.classList.add('active');
    elements.apiKeyInput.value = state.apiKey;
    elements.apiProvider.value = state.provider;
    elements.maxConcurrent.value = state.maxConcurrent;
    elements.saveHistoryCheck.checked = state.saveHistory;
}

function closeSettings() {
    elements.settingsModal.classList.remove('active');
}

function handleSaveSettings() {
    state.apiKey = elements.apiKeyInput.value.trim();
    state.provider = elements.apiProvider.value;
    state.maxConcurrent = parseInt(elements.maxConcurrent.value);
    state.saveHistory = elements.saveHistoryCheck.checked;

    saveSettings();
    closeSettings();
    showToast('설정이 저장되었습니다.', 'success');
}

function toggleApiKeyVisibility() {
    const input = elements.apiKeyInput;
    input.type = input.type === 'password' ? 'text' : 'password';
}

// ============================================================
// Image Modal
// ============================================================

let currentImageId = null;

function openImageModal(id) {
    const result = state.results.find(r => r.id === id);
    if (!result) return;

    currentImageId = id;
    elements.modalImage.src = result.isBase64 ? `data:image/png;base64,${result.url}` : result.url;
    elements.imageModal.classList.add('active');
}

window.openImageModal = openImageModal;

function closeImageModal() {
    elements.imageModal.classList.remove('active');
    currentImageId = null;
}

function downloadCurrentImage() {
    if (currentImageId) {
        downloadResult(currentImageId);
    }
}

async function copyCurrentImage() {
    const result = state.results.find(r => r.id === currentImageId);
    if (!result) return;

    try {
        const response = await fetch(result.isBase64 ? `data:image/png;base64,${result.url}` : result.url);
        const blob = await response.blob();

        await navigator.clipboard.write([
            new ClipboardItem({ [blob.type]: blob })
        ]);

        showToast('클립보드에 복사되었습니다.', 'success');
    } catch (error) {
        showToast('복사 실패', 'error');
    }
}

async function useCurrentAsReference() {
    const result = state.results.find(r => r.id === currentImageId);
    if (!result) return;

    // Switch to img2img mode
    setMode('img2img');

    // Set as reference image
    const dataUrl = result.isBase64 ? `data:image/png;base64,${result.url}` : result.url;

    // Fetch and convert to File object if it's a URL
    if (!result.isBase64) {
        try {
            const response = await fetch(result.url);
            const blob = await response.blob();
            const file = new File([blob], 'reference.png', { type: 'image/png' });

            state.referenceImages[1] = { file, dataUrl };
        } catch {
            state.referenceImages[1] = { dataUrl };
        }
    } else {
        state.referenceImages[1] = { dataUrl };
    }

    updateSlotUI(1, dataUrl);
    closeImageModal();
    showToast('참조 이미지로 설정되었습니다.', 'success');
}

// ============================================================
// History Modal
// ============================================================

function openHistory() {
    elements.historyModal.classList.add('active');
    renderHistory();
}

function closeHistory() {
    elements.historyModal.classList.remove('active');
}

function renderHistory() {
    if (state.history.length === 0) {
        elements.historyList.innerHTML = '<p style="text-align: center; color: var(--color-text-muted);">히스토리가 없습니다.</p>';
        return;
    }

    elements.historyList.innerHTML = state.history.slice().reverse().map(item => `
        <div class="history-item" onclick="restoreFromHistory('${item.id}')">
            <img src="${item.url || item.thumbnail}" class="history-thumb" alt="History">
            <div class="history-info">
                <p class="history-prompt">${item.prompt}</p>
                <span class="history-meta">${new Date(item.timestamp).toLocaleString('ko-KR')}</span>
            </div>
        </div>
    `).join('');
}

function restoreFromHistory(id) {
    const item = state.history.find(h => h.id === id);
    if (!item) return;

    elements.promptInput.value = item.prompt;
    updateCharCount();
    closeHistory();
    showToast('프롬프트가 복원되었습니다.', 'success');
}

window.restoreFromHistory = restoreFromHistory;

function handleClearHistory() {
    if (confirm('모든 히스토리를 삭제하시겠습니까?')) {
        state.history = [];
        localStorage.removeItem('seedream_history');
        updateHistoryCount();
        renderHistory();
        showToast('히스토리가 삭제되었습니다.', 'success');
    }
}

function updateHistoryCount() {
    elements.historyCount.textContent = state.history.length;
}

// ============================================================
// Toast Notifications
// ============================================================

function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    const icons = {
        success: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20,6 9,17 4,12"/></svg>',
        error: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
        warning: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
        info: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'
    };

    toast.innerHTML = `
        <span class="toast-icon">${icons[type]}</span>
        <span class="toast-message">${message}</span>
    `;

    elements.toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'toastIn 0.3s ease reverse';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// ============================================================
// Keyboard Shortcuts
// ============================================================

function handleKeydown(e) {
    // Ctrl/Cmd + Enter to generate
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        if (!state.isGenerating) {
            generate();
        }
    }

    // Escape to close modals
    if (e.key === 'Escape') {
        closeSettings();
        closeImageModal();
        closeHistory();
    }
}
