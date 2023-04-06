document.addEventListener('DOMContentLoaded', () => {
    const scrollItems = document.querySelectorAll('.scroll-item');
    const divInformation = document.querySelector('#information')
    const scrollAnimation = () => {
		let windowCenter = (window.innerHeight / 1.2) + window.scrollY;
		// console.log(windowCenter)
		scrollItems.forEach(el => {
			let scrollOffset = el.offsetTop;
			// console.log(scrollOffset)
			if (windowCenter >= scrollOffset) {
				el.classList.add('scroll-animation-class');
			} else {
				el.classList.remove('scroll-animation-class');
			}
		});
	};

    scrollAnimation();
    document.addEventListener('scroll', () => {
        scrollAnimation();
    })
});