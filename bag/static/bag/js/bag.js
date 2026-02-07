/* Same JS as product_details bag quantity controls, but applied
 to quantity controls in the bag summary on the bag page. 
*/

/* Bag quantity controls (basic: user clicks Update to submit form) */
document.addEventListener("DOMContentLoaded", () => {
  const MIN_QTY = 1;
  const MAX_QTY = 99;

  document.querySelectorAll(".quantity-wrapper").forEach((wrapper) => {
    const minusBtn = wrapper.querySelector(".qty-btn.minus");
    const plusBtn = wrapper.querySelector(".qty-btn.plus");
    const input = wrapper.querySelector(".qty-input");

    if (!minusBtn || !plusBtn || !input) return;

    const clamp = (val) => Math.min(MAX_QTY, Math.max(MIN_QTY, val));

    const sync = () => {
      const val = parseInt(input.value, 10);
      input.value = clamp(isNaN(val) ? MIN_QTY : val);
      minusBtn.disabled = parseInt(input.value, 10) <= MIN_QTY;
    };

    // Initialise
    sync();

    minusBtn.addEventListener("click", () => {
      input.value = clamp(parseInt(input.value, 10) - 1);
      sync();
    });

    plusBtn.addEventListener("click", () => {
      input.value = clamp(parseInt(input.value, 10) + 1);
      sync();
    });

    input.addEventListener("input", sync);
  });
});
