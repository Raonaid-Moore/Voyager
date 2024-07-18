let currentIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
const carouselContainer = document.querySelector('.carousel-container');
let slideInterval = setInterval(nextSlide, 5000);

function nextSlide() {
    moveSlide(1);
}

function moveSlide(n) {
    clearInterval(slideInterval);
    currentIndex += n;

    if (currentIndex >= slides.length) {
        currentIndex = 0;
    } else if (currentIndex < 0) {
        currentIndex = slides.length - 1;
    }



// Optional: Attach event listeners to buttons if needed
document.querySelector('.carousel-control.prev').addEventListener('click', () => moveSlide(-1));
document.querySelector('.carousel-control.next').addEventListener('click', () => moveSlide(1));
