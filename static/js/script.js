
document.addEventListener("DOMContentLoaded", () => {
    const notReadyLinks = document.querySelectorAll(".not-ready");
    const modal = document.getElementById("notReadyModal");
    const closeBtn = document.querySelector(".close-btn");
    notReadyLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            modal.style.display = "block";
        });
    });

    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
    });

    window.addEventListener("click", (e) => {
        if (e.target === modal) {
            modal.style.display = "none";
        }
    });
});


document.addEventListener("DOMContentLoaded", () => {
  const heroImg = document.querySelector(".hero-image img");
  const images = window.heroImages || [];
  if (!heroImg || images.length === 0) return;

  let current = 0;

  setInterval(() => {
    // Fade out
    heroImg.style.opacity = 0;

    // Wait for the fade-out transition to complete (1s)
    setTimeout(() => {
      // Change to the next image
      current = (current + 1) % images.length;
      heroImg.src = `/static/${images[current]}`;

      // Small delay before fading back in (lets browser update src)
      requestAnimationFrame(() => {
        heroImg.style.opacity = 1;
      });
    }, 1000); // matches your CSS transition duration
  }, 10000); // Change image every 10 seconds
});



