document.addEventListener("DOMContentLoaded", function () {
  const priceEl = document.getElementById("product-price");
  const singleBtn = document.getElementById("single-btn");
  const setBtn = document.getElementById("set-btn");

  // If this product has no dice buttons (bags/rollers), do nothing
  if (!priceEl || !singleBtn || !setBtn) return;

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
