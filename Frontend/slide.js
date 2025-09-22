// Slide image section

document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.projects-slider');
  if (!slider) return;

  const slides = slider.querySelectorAll('.slide');
  const slideWidth = slides[0].offsetWidth;
  let position = 0;
  let isPaused = false;
  const speed = 1; // pixels per frame
  let animationFrameId;

  function animate() {
    if (!isPaused) {
      position -= speed;
      if (Math.abs(position) >= slideWidth) {
        position += slideWidth;
        slider.appendChild(slider.firstElementChild);
      }
      slider.style.transform = `translateX(${position}px)`;
    }
    animationFrameId = requestAnimationFrame(animate);
  }

  slider.addEventListener('mouseenter', () => {
    isPaused = true;
  });

  slider.addEventListener('mouseleave', () => {
    isPaused = false;
  });

  // Initialize
  animate();
});
