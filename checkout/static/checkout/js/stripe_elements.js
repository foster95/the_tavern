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
    "::placeholder": { color: "#aab7c4" },
  },
  invalid: {
    color: "#dc3545",
    iconColor: "#dc3545",
  },
};

// Create card element
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Realtime validation errors
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  var cardElement = document.getElementById("card-element");

  if (event.error) {
    errorDiv.innerHTML = `
      <span class="icon" role="alert">
        <i class="fas fa-times"></i>
      </span>
      <span>${event.error.message}</span>
    `;
    if (cardElement) cardElement.classList.add("has-error");
  } else {
    errorDiv.textContent = "";
    if (cardElement) cardElement.classList.remove("has-error");
  }
});

var form = document.getElementById("payment-form");
var submitBtn = document.getElementById("complete-order-button");
var originalBtnHTML = submitBtn ? submitBtn.innerHTML : "";
var isSubmitting = false;

function fieldValue(id) {
  return (document.getElementById(id)?.value || "").trim();
}

form.addEventListener("submit", function (ev) {
  ev.preventDefault();

  // Prevent multiple submissions
  if (isSubmitting) return;
  isSubmitting = true;

  // Disable submit button and show spinner
  card.update({ disabled: true });
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <i class="fa-solid fa-spinner fa-spin me-2"></i>
      Processing...
    `;
  }

  var saveInfo = Boolean($("#save-info").attr("checked"));
  var csrfToken = $("input[name='csrfmiddlewaretoken']").val();

  var postData = {
    csrfmiddlewaretoken: csrfToken,
    client_secret: clientSecret,
    save_info: saveInfo,
  };

  $.post("/checkout/cache_checkout_data/", postData)
    .done(function () {
      // Confirm payment after caching
      stripe
        .confirmCardPayment(clientSecret, {
          payment_method: {
            card: card,
            billing_details: {
              name: fieldValue("id_full_name"),
              email: fieldValue("id_email"),
              phone: fieldValue("id_phone_number"),
              address: {
                line1: fieldValue("id_street_address1"),
                line2: fieldValue("id_street_address2"),
                city: fieldValue("id_town_or_city"),
                state: fieldValue("id_county"),
                country: fieldValue("id_country"),
              },
            },
          },

          shipping: {
            name: fieldValue("id_full_name"),
            phone: fieldValue("id_phone_number"),
            address: {
              line1: fieldValue("id_street_address1"),
              line2: fieldValue("id_street_address2"),
              city: fieldValue("id_town_or_city"),
              state: fieldValue("id_county"),
              postal_code: fieldValue("id_postcode"),
              country: fieldValue("id_country"),
            },
          },
        })
        .then(function (result) {
          if (result.error) {
            // Show error
            var errorDiv = document.getElementById("card-errors");
            errorDiv.innerHTML = `
              <span class="icon" role="alert">
                <i class="fas fa-times"></i>
              </span>
              <span>${result.error.message}</span>
            `;

            card.update({ disabled: false });
            if (submitBtn) {
              submitBtn.disabled = false;
              submitBtn.innerHTML = originalBtnHTML;
            }
            isSubmitting = false;
          } else {
            form.submit();
          }
        })
        .catch(function () {
          card.update({ disabled: false });
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnHTML;
          }
          isSubmitting = false;
        });
    })
    .fail(function () {
      location.reload();
    });
});
