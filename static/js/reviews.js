document.getElementById('add-review-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get form values
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const rating = document.getElementById('rating').value;
    const reviewText = document.getElementById('review').value;

    // Create new review elements
    const reviewContainer = document.createElement('div');
    reviewContainer.className = 'review';

    const reviewHeader = document.createElement('div');
    reviewHeader.className = 'review-header';

    const reviewerDetails = document.createElement('div');
    reviewerDetails.className = 'reviewer-details';

    const reviewerName = document.createElement('h2');
    reviewerName.textContent = name;

    const reviewDate = document.createElement('p');
    reviewDate.textContent = `Reviewed on ${new Date(date).toLocaleDateString()}`;

    reviewerDetails.appendChild(reviewerName);
    reviewerDetails.appendChild(reviewDate);

    const reviewRating = document.createElement('div');
    reviewRating.className = 'review-rating';
    reviewRating.textContent = '★'.repeat(rating) + '☆'.repeat(5 - rating);

    reviewHeader.appendChild(reviewerDetails);
    reviewHeader.appendChild(reviewRating);

    const reviewTextElement = document.createElement('p');
    reviewTextElement.className = 'review-text';
    reviewTextElement.textContent = reviewText;

    reviewContainer.appendChild(reviewHeader);
    reviewContainer.appendChild(reviewTextElement);

    // Add new review to the reviews container
    document.querySelector('.reviews-container').appendChild(reviewContainer);

    // Clear form
    document.getElementById('add-review-form').reset();
});
