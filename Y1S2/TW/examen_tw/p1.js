document.addEventListener('DOMContentLoaded', () => {
    const divs = document.querySelectorAll('#parinte > div');

    divs.forEach((div, index) => {
        if (index % 2 === 0) {
            div.addEventListener('mouseover', () => {
                div.style.transition = 'all 3s';
                div.style.backgroundColor = 'blue';
                div.style.fontWeight = 'bold';
            });

            div.addEventListener('mouseout', () => {
                div.style.transition = 'all 3s';
                div.style.backgroundColor = '';
                div.style.fontWeight = '';
            });
        }
    });
});