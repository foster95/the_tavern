/**
 * Handles price switching on the product detail page
 * between single dice and full set options.
 */

document.addEventListener("DOMContentLoaded", function () {
  const priceEl = document.getElementById("product-price");
  const singleBtn = document.getElementById("single-btn");
  const setBtn = document.getElementById("set-btn");

  if (!priceEl || !singleBtn || !setBtn) return;

  /**
   * Activates one button, deactivates the other,
   * and updates the displayed price.
   */
  
  function pick(activeBtn, otherBtn) {
    activeBtn.classList.add("active");
    otherBtn.classList.remove("active");
    priceEl.textContent = activeBtn.dataset.price;
  }

  singleBtn.addEventListener("click", function () {
    pick(singleBtn, setBtn);
  });

  setBtn.addEventListener("click", function () {
    pick(setBtn, singleBtn);
  });
});
