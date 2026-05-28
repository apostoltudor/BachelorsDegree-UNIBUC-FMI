document.addEventListener('DOMContentLoaded', () => {
    const paragraph = document.getElementById('info');
    let intervalId;
    let dateAdded = false;
    let resizingActive = false; 

    const savedFontSize = localStorage.getItem('fontSize');
    if (savedFontSize) {
        paragraph.style.fontSize = `${savedFontSize}px`;
    }

    document.addEventListener('keydown', (event) => {
        if (event.key === 'a') {
            if (!dateAdded) {
                const currentDate = new Date();
                paragraph.textContent += ` ${currentDate.toLocaleString()}`;
                dateAdded = true; 

                intervalId = setInterval(() => {
                    const fontSize = Math.floor(Math.random() * 21) + 10; 
                    paragraph.style.fontSize = `${fontSize}px`;
                }, 3000);
                resizingActive = true; 
            } else if (resizingActive) {
                clearInterval(intervalId);
                resizingActive = false; 

                const currentFontSize = window.getComputedStyle(paragraph).fontSize;
                localStorage.setItem('fontSize', parseInt(currentFontSize));
            }
        }
    });
});