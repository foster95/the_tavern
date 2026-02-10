// 1) Read keys safely from the Django template
const stripePublicKey = JSON.parse(
  document.getElementById("stripe-public-key").textContent
);
const clientSecret = JSON.parse(
  document.getElementById("client-secret").textContent
);

// 2) Create Stripe + Elements
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

// 3) Create Card Element and mount into your existing <div id="card-element">
const card = elements.create("card");
card.mount("#card-element");

// 4) Show card validation errors under the element
card.on("change", (event) => {
  const errorDiv = document.getElementById("card-errors");
  errorDiv.textContent = event.error ? event.error.message : "";
});

// 5) Confirm payment on form submit
const form = document.getElementById("payment-form");
const submitBtn = document.getElementById("complete-order-button");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  // UI lock
  submitBtn.disabled = true;

  // Optional: clear any old errors
  document.getElementById("card-errors").textContent = "";

  // Confirm the PaymentIntent using the card element
  const { paymentIntent, error } = await stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
      billing_details: {
        name: document.getElementById("id_full_name")?.value || "",
        email: document.getElementById("id_email")?.value || "",
        phone: document.getElementById("id_phone_number")?.value || "",
      },
    },
  });

  if (error) {
    document.getElementById("card-errors").textContent = error.message;
    submitBtn.disabled = false;
    return;
  }

  // Success: attach PI id to the form so Django can save it, then submit
  const hidden = document.createElement("input");
  hidden.type = "hidden";
  hidden.name = "payment_intent_id";
  hidden.value = paymentIntent.id;
  form.appendChild(hidden);

  form.submit();
});
