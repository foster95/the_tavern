document.addEventListener("DOMContentLoaded", function () {

    /* -----------------------------
       QUANTITY BUTTONS
    ----------------------------- */
    const minusBtns = document.querySelectorAll(".qty-btn.minus");
    const plusBtns = document.querySelectorAll(".qty-btn.plus");

    minusBtns.forEach(btn => {
        btn.addEventListener("click", function () {
            const input = this.nextElementSibling;
            let value = parseInt(input.value) || 1;
            if (value > 1) input.value = value - 1;
        });
    });

    plusBtns.forEach(btn => {
        btn.addEventListener("click", function () {
            const input = this.previousElementSibling;
            let value = parseInt(input.value) || 1;
            if (value < 99) input.value = value + 1;
        });
    });


    /* -----------------------------
       STAR RATING INPUT (WRITE REVIEW)
    ----------------------------- */
    const stars = document.querySelectorAll("#star-rating i");
    const ratingInput = document.querySelector("#id_rating");

    function paintStars(starNodeList, value) {
        starNodeList.forEach((star, index) => {
            if (index < value) {
                star.classList.remove("far");
                star.classList.add("fas");
            } else {
                star.classList.remove("fas");
                star.classList.add("far");
            }
        });
    }

    if (stars.length && ratingInput) {

        // Click to select rating
        stars.forEach(star => {
            star.addEventListener("click", function () {
                const value = parseInt(this.dataset.value);
                ratingInput.value = value;
                paintStars(stars, value);
            });

            // Hover preview
            star.addEventListener("mouseenter", function () {
                paintStars(stars, parseInt(this.dataset.value));
            });

            // Keyboard accessibility
            star.addEventListener("keydown", function (e) {
                if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    const value = parseInt(this.dataset.value);
                    ratingInput.value = value;
                    paintStars(stars, value);
                }
            });
        });

        // Reset after hover
        const wrapper = document.getElementById("star-rating");
        if (wrapper) {
            wrapper.addEventListener("mouseleave", function () {
                paintStars(stars, parseInt(ratingInput.value || 0));
            });
        }
    }


    /* -----------------------------
       PRODUCT AVERAGE RATING STARS
    ----------------------------- */
    const avgWrappers = document.querySelectorAll(".js-average-rating");

    avgWrappers.forEach(wrapper => {
        const rating = parseFloat(wrapper.dataset.rating || "0");
        const rounded = Math.round(rating);
        const avgStars = wrapper.querySelectorAll("i");

        paintStars(avgStars, rounded);
    });

});


/* -----------------------------
   DELETE REVIEW MODAL
----------------------------- */
document.addEventListener("DOMContentLoaded", function () {
    const modalEl = document.getElementById("deleteReviewModal");
    const formEl = document.getElementById("deleteReviewForm");

    if (!modalEl || !formEl) return;

    modalEl.addEventListener("show.bs.modal", function (event) {
        const trigger = event.relatedTarget;
        if (!trigger) return;

        const deleteUrl = trigger.getAttribute("data-delete-url");
        if (deleteUrl) {
            formEl.setAttribute("action", deleteUrl);
        }
    });
});
