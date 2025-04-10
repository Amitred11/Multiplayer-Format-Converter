const form = document.getElementById('uploadForm');
const progress = document.getElementById('progress');
const progressBar = document.getElementById('progress-bar');
const message = document.getElementById('message');
const historyList = document.getElementById('history-list');
const errorPopup = document.getElementById('error-popup');
const errorMessage = document.getElementById('error-message');
const clearHistoryButton = document.getElementById('clear-history');

function addHistoryItem(url, filename) {
    const li = document.createElement('li');
    li.className = 'history-item';
    li.innerHTML = `<a href="${url}" download="${filename}">${filename}</a>`;
    historyList.prepend(li);
    const historyItems = document.querySelectorAll('.history-item');
    historyItems.forEach((item, index) => {
        item.style.setProperty('--index', index);
    });
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    progress.style.display = 'block';
    progressBar.style.width = '10%';
    message.style.display = 'none';

    const formData = new FormData(form);
    try {
        const response = await fetch('/convert', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorText = await response.text();
            showErrorPopup(`Conversion failed: ${errorText || 'Unknown error'}`);
            progress.style.display = 'none';
            progressBar.style.width = '0%';
            return;
        }

        progressBar.style.width = '50%';

        const blob = await response.blob();
        const filename = response.headers.get('X-Filename');
        const url = window.URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);

        addHistoryItem(url, filename);

        progressBar.style.width = '100%';
        setTimeout(() => {
            progress.style.display = 'none';
            progressBar.style.width = '0%';
        }, 1000);

    } catch (error) {
        console.error("Fetch error:", error);
        showErrorPopup('An unexpected error occurred during conversion. Please try again.');
        progress.style.display = 'none';
        progressBar.style.width = '0%';
    }
});

function showErrorPopup(messageText) {
    errorMessage.innerText = messageText;
    errorPopup.style.display = 'block';
}

function closeErrorPopup() {
    errorPopup.style.display = 'none';
}

clearHistoryButton.addEventListener('click', () => {
    historyList.innerHTML = '';
});

const initialHistoryItems = document.querySelectorAll('.history-item');
initialHistoryItems.forEach((item, index) => {
    item.style.setProperty('--index', index);
});
