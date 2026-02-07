/* Same JS as product_details bag quantity controls, but applied
 to quantity controls in the bag summary on the bag page. 
 This ensures consistent behavior across both pages and prevents
 invalid quantities from being submitted when updating the bag
 from the bag summary.
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