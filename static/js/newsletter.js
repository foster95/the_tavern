document.addEventListener("DOMContentLoaded", function () {
  const MAILCHIMP_POST_JSON =
    "https://herokuapp.us3.list-manage.com/subscribe/post-json?u=8c064234998503bf3de9f0fb7&id=bc9744133c&f_id=00afb4e3f0";

  const form = document.getElementById("mc-subscribe-form");
  if (!form) return; // prevents errors on pages without footer

  const emailInput = document.getElementById("mc-email");
  const alertBox = document.getElementById("mc-alert");
  const submitBtn = document.getElementById("mc-submit");

  function show(message, ok) {
    alertBox.classList.remove("d-none", "alert-success", "alert-danger");
    alertBox.classList.add(ok ? "alert-success" : "alert-danger");
    alertBox.textContent = message;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const email = emailInput.value.trim();
    if (!email) {
      show("Please enter an email address.", false);
      return;
    }

    submitBtn.disabled = true;

    const cbName = "mc_cb_" + Date.now();
    const script = document.createElement("script");

    window[cbName] = function (data) {
      if (data.result === "success") {
        show("Welcome adventurer - you're now subscribed to our newsletter!", true);
        form.reset();
      } else {
        const tmp = document.createElement("div");
        tmp.innerHTML = data.msg || "Something went wrong.";
        show(tmp.textContent, false);
      }

      submitBtn.disabled = false;
      delete window[cbName];
      script.remove();
    };

    script.src =
      MAILCHIMP_POST_JSON +
      "&c=" + encodeURIComponent(cbName) +
      "&EMAIL=" + encodeURIComponent(email);

    document.body.appendChild(script);
  });
});