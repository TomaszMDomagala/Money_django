const hamburger = document.querySelector('.hamburger');
const navigation = document.querySelector('.navigation');
const handleClicking = () => {
	hamburger.classList.toggle('hamburger--active');
	navigation.classList.toggle('navigation--active');
}
hamburger.addEventListener('click', handleClicking);