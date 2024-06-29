const darkModeToggle = document.querySelector('.dark-mode-toggle');
const darkModeIcon = darkModeToggle.querySelector('i');
const html = document.documentElement;
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileList = document.getElementById('fileList');
const processButton = document.getElementById('processButton');
const popup = document.getElementById('popup');
const popupImage = document.getElementById('popupImage');
const imageInfo = document.getElementById('imageInfo');
const prevButton = document.getElementById('prevButton');
const nextButton = document.getElementById('nextButton');
const alertPopup = document.getElementById('alertPopup');
const resetButton = document.getElementById('resetButton');
const okButton = document.getElementById('okButton');

let selectedFiles = [];
let currentImageIndex = 0;
let results = [];

darkModeToggle.addEventListener('click', () => {
    html.classList.toggle('dark');
    updateDarkModeIcon();
});

function updateDarkModeIcon() {
    const isDark = html.classList.contains('dark');
    darkModeIcon.setAttribute('data-feather', isDark ? 'moon' : 'sun');
    darkModeIcon.classList.toggle('text-yellow-400', !isDark);
    darkModeIcon.classList.toggle('text-blue-300', isDark);
    feather.replace();
}

feather.replace();

dropZone.addEventListener('click', () => fileInput.click());
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragging');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragging'));
dropZone.addEventListener('drop', handleDrop);
fileInput.addEventListener('change', handleFileSelect);
processButton.addEventListener('click', processFiles);
prevButton.addEventListener('click', showPreviousImage);
nextButton.addEventListener('click', showNextImage);
resetButton.addEventListener('click', resetFiles);
okButton.addEventListener('click', () => popup.classList.remove('show'));

function handleDrop(e) {
    e.preventDefault();
    dropZone.classList.remove('dragging');
    handleFiles(e.dataTransfer.files);
}

function handleFileSelect(e) {
    handleFiles(e.target.files);
}

function handleFiles(files) {
    selectedFiles = Array.from(files).filter(file => file.type.startsWith('image/'));
    fileList.innerHTML = '';
    for (const file of selectedFiles) {
        const div = document.createElement('div');
        div.className = 'file-item';
        div.innerHTML = `<span class="file-name">${file.name}</span><span class="file-type">${file.type}</span>`;
        fileList.appendChild(div);
    }
}

async function processFiles() {
    if (selectedFiles.length === 0) {
        showAlert();
        return;
    }

    const formData = new FormData();
    selectedFiles.forEach(file => formData.append('files', file));

    const selectedOptions = Array.from(document.querySelectorAll('input[name="options"]:checked')).map(checkbox => checkbox.value);
    formData.append('options', JSON.stringify(selectedOptions));

    try {
        const response = await fetch('/process', {
            method: 'POST',
            body: formData,
        });
        results = await response.json();
        currentImageIndex = 0;
        showImage(currentImageIndex);
        popup.classList.add('show');
    } catch (error) {
        console.error('Error processing files:', error);
    }
}

function showImage(index) {
    const file = selectedFiles[index];
    const reader = new FileReader();
    reader.onload = (e) => {
        popupImage.src = e.target.result;
        showImageInfo(results[index]);
    };
    reader.readAsDataURL(file);
    updateNavigationButtons();
}

function showImageInfo(info) {
    // imageInfo.innerHTML = `
    //     <p><strong>Filename:</strong> ${info.filename}</p>
    //     <p><strong>Size:</strong> ${info.size} bytes</p>
    //     <p><strong>Type:</strong> ${info.type}</p>
    //     <p><strong>Info:</strong> ${info.info}</p>
    // // `;
    // imageInfo.innerHTML = `
    //     Chum Khò
    // `;
    imageInfo.innerHTML = `
        <p><strong>Info:</strong> ${info.info}</p> `;
}

function showPreviousImage() {
    if (currentImageIndex > 0) {
        currentImageIndex--;
        showImage(currentImageIndex);
    }
}

function showNextImage() {
    if (currentImageIndex < selectedFiles.length - 1) {
        currentImageIndex++;
        showImage(currentImageIndex);
    }
}

function updateNavigationButtons() {
    prevButton.disabled = currentImageIndex === 0;
    nextButton.disabled = currentImageIndex === selectedFiles.length - 1;
}

popup.addEventListener('click', (e) => {
    if (e.target === popup) {
        popup.classList.remove('show');
    }
});

function showAlert() {
    alertPopup.style.display = 'block';
    setTimeout(() => alertPopup.style.display = 'none', 2000);
}

function resetFiles() {
    selectedFiles = [];
    fileList.innerHTML = '';
    popup.classList.remove('show');
}

document.addEventListener('DOMContentLoaded', function() {
    const selectAllCheckbox = document.getElementById('select-all');
    const checkboxes = document.querySelectorAll('.checkbox-group input[type="checkbox"]:not(#select-all)');

    selectAllCheckbox.addEventListener('change', function() {
        checkboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
    });

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (!checkbox.checked) {
                selectAllCheckbox.checked = false;
            } else {
                const allChecked = Array.from(checkboxes).every(checkbox => checkbox.checked);
                selectAllCheckbox.checked = allChecked;
            }
        });
    });
});

// Add these variables at the beginning of the script
const progressPopup = document.getElementById('progressPopup');
const progressCircle = document.querySelector('.progress-ring__circle');
const radius = progressCircle.r.baseVal.value;
const circumference = 2 * Math.PI * radius;
const progressText = document.getElementById('progressText');

progressCircle.style.strokeDasharray = `${circumference} ${circumference}`;
progressCircle.style.strokeDashoffset = circumference;

function setProgress(percent) {
    const integerPercent = Math.round(percent);
    const offset = circumference - (integerPercent / 100) * circumference;
    progressCircle.style.strokeDashoffset = offset;
    progressText.textContent = `${integerPercent}%`;
}

function showProgressPopup(imageCount) {
    progressPopup.classList.add('show');
    setProgress(0);
    let progress = 0;
    const interval = setInterval(() => {
        progress += 1/imageCount;
        setProgress(progress);
        if (progress >= 97) {
            clearInterval(interval);
        }
    }, 97);
    return interval;
}

function hideProgressPopup(interval) {
    clearInterval(interval);
    progressPopup.classList.remove('show');
    setProgress(100);
}

async function processFiles() {
    if (selectedFiles.length === 0) {
        showAlert();
        return;
    }

    const formData = new FormData();
    selectedFiles.forEach(file => formData.append('files', file));

    const selectedOptions = Array.from(document.querySelectorAll('input[name="options"]:checked')).map(checkbox => checkbox.value);
    formData.append('options', JSON.stringify(selectedOptions));

    try {
        const interval = showProgressPopup(selectedFiles.length);
        const response = await fetch('/process', {
            method: 'POST',
            body: formData,
        });
        results = await response.json();
        hideProgressPopup(interval);
        currentImageIndex = 0;
        showImage(currentImageIndex);
        popup.classList.add('show');
    } catch (error) {
        console.error('Error processing files:', error);
    }
}
