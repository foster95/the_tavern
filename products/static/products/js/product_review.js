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
       DICE OPTION PRICE SWITCH
    ----------------------------- */
    const singleBtn = document.getElementById("single-btn");
    const setBtn = document.getElementById("set-btn");
    const priceEl = document.getElementById("product-price");
    const diceInput = document.getElementById("dice-option");

    function selectOption(button, other, value, price) {
        button.classList.add("active");
        if (other) other.classList.remove("active");

        if (priceEl && price) priceEl.textContent = parseFloat(price).toFixed(2);
        if (diceInput) diceInput.value = value;
    }

    if (singleBtn && setBtn) {
        singleBtn.addEventListener("click", function () {
            selectOption(singleBtn, setBtn, "single", this.dataset.price);
        });

        setBtn.addEventListener("click", function () {
            selectOption(setBtn, singleBtn, "set", this.dataset.price);
        });

        // default highlight
        selectOption(singleBtn, setBtn, "single", singleBtn.dataset.price);
    }


    /* -----------------------------
       STAR RATING INPUT
    ----------------------------- */
    const stars = document.querySelectorAll("#star-rating i");
    const ratingInput = document.querySelector("#id_rating");

    if (stars.length && ratingInput) {

        function paintStars(value) {
            stars.forEach((star, index) => {
                if (index < value) {
                    star.classList.remove("far");
                    star.classList.add("fas");
                } else {
                    star.classList.remove("fas");
                    star.classList.add("far");
                }
            });
        }

        // Click to select rating
        stars.forEach(star => {
            star.addEventListener("click", function () {
                const value = parseInt(this.dataset.value);
                ratingInput.value = value;
                paintStars(value);
            });

            // Hover preview
            star.addEventListener("mouseenter", function () {
                paintStars(parseInt(this.dataset.value));
            });

            // Keyboard accessibility (Enter / Space)
            star.addEventListener("keydown", function (e) {
                if (e.key === "Enter" || e.key === " ") {
                    e.preventDefault();
                    const value = parseInt(this.dataset.value);
                    ratingInput.value = value;
                    paintStars(value);
                }
            });
        });

        // Reset after hover
        const wrapper = document.getElementById("star-rating");
        wrapper.addEventListener("mouseleave", function () {
            paintStars(parseInt(ratingInput.value || 0));
        });
    }

});

document.addEventListener("DOMContentLoaded", function () {
  const modalEl = document.getElementById("deleteReviewModal");
  const formEl = document.getElementById("deleteReviewForm");

  if (!modalEl || !formEl) return;

  modalEl.addEventListener("show.bs.modal", function (event) {
    const trigger = event.relatedTarget; // the button that opened the modal
    if (!trigger) return;

    const deleteUrl = trigger.getAttribute("data-delete-url");
    if (deleteUrl) {
      formEl.setAttribute("action", deleteUrl);
    }
  });
});

