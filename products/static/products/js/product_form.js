document.addEventListener("DOMContentLoaded", function () {

    function initDiceToggle() {

        const checkbox = document.getElementById("id_is_dice_set");
        const setPrice = document.getElementById("set-price");

        if (!checkbox || !setPrice) return;

        function togglePrices() {
            if (checkbox.checked) {
                setPrice.classList.remove("d-none");
            } else {
                setPrice.classList.add("d-none");
            }
        }

        togglePrices();

        checkbox.addEventListener("change", togglePrices);
    }

    setTimeout(initDiceToggle, 50);
});

document.addEventListener("DOMContentLoaded", function() {

    const setPrice = document.getElementById("set-price");
    const priceInput = document.getElementById("id_dice_set_price");

    if (!setPrice || !priceInput) return;

    priceInput.addEventListener("input", function() {
        if (priceInput.value) {
            setPrice.classList.remove("d-none");
        }
    });

});
