/* jshint esversion: 6 */
/* global bootstrap */

/* Bag quantity controls + prevent Update if quantity hasn't changed */

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

  let warningShown = false;

  document.querySelectorAll("form").forEach((form) => {
    const input = form.querySelector(".qty-input");
    const updateBtn = form.querySelector(".bag-update-button, .update-button");

    if (!input || !updateBtn) return;

    input.addEventListener("input", () => {
      warningShown = false;
    });

    form.addEventListener("submit", (e) => {
      const original = parseInt(input.dataset.original, 10);
      const current = parseInt(input.value, 10);

      if (isNaN(original)) return;

      if (original === current) {
        e.preventDefault();

        if (!warningShown) {
          showBagMessage("Quantity hasn’t changed.");
          warningShown = true;
        }
      }
    });
  });
});

function showBagMessage(text) {
  const toastEl = document.getElementById("js-toast-warning");
  const textEl = document.getElementById("js-toast-warning-text");

  if (!toastEl || !textEl) return;

  textEl.textContent = text;

  toastEl.classList.remove("d-none");

  const toast = bootstrap.Toast.getOrCreateInstance(toastEl);
  toast.show();
}

document.addEventListener("DOMContentLoaded", () => {
  const toastEl = document.getElementById("js-toast-warning");
  if (!toastEl) return;

  toastEl.addEventListener("hidden.bs.toast", () => {
    toastEl.classList.add("d-none");
  });
});