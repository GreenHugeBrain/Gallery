<<<<<<< HEAD
document.querySelector('.img').addEventListener('click', () => {
    document.querySelector('.img').classList.toggle('absolute');
=======
document.querySelector('.img').addEventListener('click', () => {
    const img = document.querySelector('.img');
    const rect = img.getBoundingClientRect(); // Get dimensions of the image
    const x = window.innerWidth / 2 - rect.width / 2; // Calculate center horizontally
    const y = window.innerHeight / 2 - rect.height / 2; // Calculate center vertically

    // Toggle position to absolute and center it
    if (img.style.position === 'absolute') {
        img.style.position = 'relative';
        img.style.left = 'auto';
        img.style.top = 'auto';
    } else {
        img.style.position = 'absolute';
        img.style.left = x + 'px';
        img.style.top = y + 'px';
    }

    // Additional CSS styles
    img.style.transition = 'all 0.3s ease'; // Smooth transition
    img.style.transformOrigin = 'center center'; // Transform origin at the center
>>>>>>> 43c4bf602e8e9ef152702ba65fd824b8ea2a4d4d
});