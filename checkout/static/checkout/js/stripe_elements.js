// Keys from Django json_script 
var stripePublicKey = JSON.parse(
  document.getElementById("stripe-public-key").textContent
);
var clientSecret = JSON.parse(
  document.getElementById("client-secret").textContent
);

// Stripe setup
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Style 
var style = {
  base: {
    color: "#1A1A1D",
    fontFamily: "'Montserrat', sans-serif",
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4",
    },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};

// Create card element
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle realtime validation errors on the card element
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  var cardElement = document.getElementById("card-element");

  if (event.error) {
    var html = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
    `;
    errorDiv.innerHTML = html;
    if (cardElement) cardElement.classList.add("has-error");
  } else {
    errorDiv.textContent = "";
    if (cardElement) cardElement.classList.remove("has-error");
  }
});

// Handle form submit and double-submit protection
var form = document.getElementById("payment-form");
var submitBtn = document.getElementById("complete-order-button");

// keep original label so we can restore it
var originalBtnHTML = submitBtn ? submitBtn.innerHTML : "";
var isSubmitting = false;

form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  // Prevent multiple submissions
  if (isSubmitting) return;
  isSubmitting = true;

  // Disable card + button
  card.update({ disabled: true });
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <i class="fa-solid fa-spinner fa-spin me-2"></i>
      Processing...
    `;
  }

  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          name: document.getElementById("id_full_name")?.value || "",
          email: document.getElementById("id_email")?.value || "",
          phone: document.getElementById("id_phone_number")?.value || "",
        },
      },
    })
    .then(function (result) {
      if (result.error) {
        // Show error
        var errorDiv = document.getElementById("card-errors");
        var html = `
          <span class="icon" role="alert">
            <i class="fas fa-times"></i>
          </span>
          <span>${result.error.message}</span>
        `;
        errorDiv.innerHTML = html;

        // Re-enable so user can try again
        card.update({ disabled: false });
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnHTML;
        }
        isSubmitting = false;
      } else {
        // Success
        if (result.paymentIntent && result.paymentIntent.status === "succeeded") {
          // Attach PI id so Django can store it 
          var hidden = document.createElement("input");
          hidden.type = "hidden";
          hidden.name = "payment_intent_id";
          hidden.value = result.paymentIntent.id;
          form.appendChild(hidden);

          form.submit();
        } else {
          // Unexpected status: allow retry
          card.update({ disabled: false });
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnHTML;
          }
          isSubmitting = false;
        }
      }
    })
    .catch(function () {
      // Any unexpected JS/network error: unlock UI
      card.update({ disabled: false });
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnHTML;
      }
      isSubmitting = false;
    });
});
