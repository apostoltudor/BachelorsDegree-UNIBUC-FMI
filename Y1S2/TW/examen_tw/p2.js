
document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;

    for (let i = 1; i <= 6; i++) {
        const button = document.createElement('button');
        button.style.height = '40px';
        button.style.width = '100px';
        button.style.borderRadius = '10px';
        button.style.marginRight = '10px';
        button.id = `buton${i}`;
        button.className = 'buton';
        button.textContent = `Buton ${i}`;

        if (i % 2 === 0) {
            button.style.backgroundColor = 'green';
            button.style.color = 'white';
        } else {
            button.style.backgroundColor = 'yellow';
            button.style.color = 'black';
        }

        button.addEventListener('click', () => {
            button.style.transition = 'background-color 5s';
            button.style.backgroundColor = 'red';

            setTimeout(() => {
                if (button.style.backgroundColor === 'red') {
                    if (i % 2 === 0) {
                        button.style.backgroundColor = 'green';
                        button.style.color = 'white';
                    } else {
                        button.style.backgroundColor = 'yellow';
                        button.style.color = 'black';
                    }
                }
            }, 5000);
        });

        

        body.appendChild(button);
    }



    document.addEventListener('click', (event) => {
        if (event.target.classList.contains('buton')) {
            setTimeout(() => {
                if (event.target.style.backgroundColor === 'red') {
                    event.target.remove();
                }
            }, 5000);
        } else {
            alert(`Numarul de butoane existente: ${document.querySelectorAll('.buton').length}`);
        }
    });
});