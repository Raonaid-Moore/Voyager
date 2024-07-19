// Image carousel
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

    carouselContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
    slideInterval = setInterval(nextSlide, 5000); // Reset interval
}

document.querySelector('.carousel-control.prev').addEventListener('click', () => moveSlide(-1));
document.querySelector('.carousel-control.next').addEventListener('click', () => moveSlide(1));

// Reviews carousel
let reviewIndex = 0;
const reviewSlides = document.querySelectorAll('#reviews .carousel-slide .review');
const totalReviewSlides = reviewSlides.length;

function showReviewSlide(index) {
    const slideWidth = reviewSlides[0].clientWidth;
    const newTransform = -index * slideWidth;
    document.querySelector('#reviews .carousel-slide').style.transform = `translateX(${newTransform}px)`;
}

function nextReviewSlide() {
    reviewIndex = (reviewIndex + 1) % totalReviewSlides;
    showReviewSlide(reviewIndex);
}

function prevReviewSlide() {
    reviewIndex = (reviewIndex - 1 + totalReviewSlides) % totalReviewSlides;
    showReviewSlide(reviewIndex);
}

// Initial display for reviews carousel
showReviewSlide(reviewIndex);
