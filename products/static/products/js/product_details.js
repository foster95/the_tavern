/* jshint esversion: 6 */
/**
 * Handles price switching on the product detail page
 * between single dice and full set options.
 */

document.addEventListener("DOMContentLoaded", () => {
  const singleBtn = document.getElementById("single-btn");
  const setBtn = document.getElementById("set-btn");
  const priceSpan = document.getElementById("product-price");
  const diceOption = document.getElementById("dice-option");

  if (!singleBtn || !setBtn || !priceSpan || !diceOption) return;

  diceOption.value = "single";
  singleBtn.classList.add("active");
  setBtn.classList.remove("active");

  singleBtn.addEventListener("click", () => {
    diceOption.value = "single";
    priceSpan.textContent = singleBtn.dataset.price;

    singleBtn.classList.add("active");
    setBtn.classList.remove("active");
  });

  setBtn.addEventListener("click", () => {
    diceOption.value = "set";
    priceSpan.textContent = setBtn.dataset.price;

    setBtn.classList.add("active");
    singleBtn.classList.remove("active");
  });
});

/**
 * Handles quantity increment and decrement
 * on the product detail page.
 */

/**
 * Quantity controls for product detail page
 * - Minimum: 1
 * - Maximum: 99
 * - Disables minus button at 1
 * - Prevents manual entry of invalid values
 */

document.addEventListener("DOMContentLoaded", () => {
  const MIN_QTY = 1;
  const MAX_QTY = 99;

  document.querySelectorAll(".quantity-wrapper").forEach((wrapper) => {
    const minusBtn = wrapper.querySelector(".qty-btn.minus");
    const plusBtn = wrapper.querySelector(".qty-btn.plus");
    const input = wrapper.querySelector(".qty-input");

    if (!minusBtn || !plusBtn || !input) return;

    const updateButtons = () => {
      minusBtn.disabled = parseInt(input.value) <= MIN_QTY;
    };

    if (!input.value || parseInt(input.value) < MIN_QTY) {
      input.value = MIN_QTY;
    }
    updateButtons();

    // Minus click
    minusBtn.addEventListener("click", () => {
      let value = parseInt(input.value);

      if (value > MIN_QTY) {
        input.value = value - 1;
      }

      updateButtons();
    });

    // Plus click
    plusBtn.addEventListener("click", () => {
      let value = parseInt(input.value);

      if (value < MAX_QTY) {
        input.value = value + 1;
      }

      updateButtons();
    });

    // Disallow invalid manual input
    input.addEventListener("input", () => {
      let value = parseInt(input.value);

      if (isNaN(value) || value < MIN_QTY) {
        input.value = MIN_QTY;
      }

      if (value > MAX_QTY) {
        input.value = MAX_QTY;
      }

      updateButtons();
    });
  });
});