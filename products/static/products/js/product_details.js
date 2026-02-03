/**
 * Handles price switching on the product detail page
 * between single dice and full set options.
 */

document.addEventListener("DOMContentLoaded", () => {
  const singleBtn = document.getElementById("single-btn");
  const setBtn = document.getElementById("set-btn");
  const priceSpan = document.getElementById("product-price");
  const diceOption = document.getElementById("dice-option");

  // Only run on products that actually have the option selector
  if (!singleBtn || !setBtn || !priceSpan || !diceOption) return;

  // default is single
  diceOption.value = "single";

  singleBtn.addEventListener("click", () => {
    diceOption.value = "single";
    priceSpan.textContent = singleBtn.dataset.price;
  });

  setBtn.addEventListener("click", () => {
    diceOption.value = "set";
    priceSpan.textContent = setBtn.dataset.price;
  });
});
