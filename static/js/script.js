
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

