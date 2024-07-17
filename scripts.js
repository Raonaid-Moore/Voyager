document.addEventListener('DOMContentLoaded', function() {
    const readMoreBtn = document.querySelector('.read-more-btn');
    const hiddenText = document.querySelector('.text.hidden');

    readMoreBtn.addEventListener('click', function() {
        if (hiddenText.style.display === 'none' || hiddenText.style.display === '') {
            hiddenText.style.display = 'block';
            readMoreBtn.textContent = 'Read Less';
        } else {
            hiddenText.style.display = 'none';
            readMoreBtn.textContent = 'Read More';
        }
    });
});