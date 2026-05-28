document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('sortForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const wordsInput = document.getElementById('wordsInput').value.trim();
        const sortOption = document.getElementById('sortOption').value;

        if (!/^[a-zA-Z\s]+$/.test(wordsInput)) {
            resultDiv.textContent = 'Date invalide';
            return;
        }

        let wordsArray = wordsInput.split(/\s+/);

        if (sortOption === 'alfabetic') {
            wordsArray.sort();
        } else if (sortOption === 'lungime') {
            wordsArray.sort((a, b) => a.length - b.length);
        }

        resultDiv.textContent = wordsArray.join(' ');
    });
});