// Use IntersectionObserver to observe when an element is scrolled into view for the User
// Code adapted from 'Subtle, yet Beautiful Scroll Animations' by Beyond Fireship:
// https://www.youtube.com/watch?v=T33NN_pPeNI
const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-animation-go');
        }
    });
});

const scrollAnimationElements = document.querySelectorAll('.scroll-animation');
scrollAnimationElements.forEach((el) => scrollObserver.observe(el));
