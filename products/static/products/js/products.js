/* jshint esversion: 6 */

document.addEventListener("DOMContentLoaded", function () {
  /**
 * Handles product list sorting.
 * Updates the URL query params (sort & direction)
 * and reloads the page with a small delay.
 */

    const sortSelector = document.getElementById("sort-selector");
  if (!sortSelector) return;

  
  /**
   * Navigate to a URL with a short delay
   * to make the reload feel less abrupt.
   */

  function goTo(url) {
    setTimeout(() => {
      window.location.assign(url);
    }, 150);
  }

  sortSelector.addEventListener("change", function () {
    const currentUrl = new URL(window.location.href);

    if (this.value === "reset") {
      currentUrl.searchParams.delete("sort");
      currentUrl.searchParams.delete("direction");
      goTo(currentUrl.toString());
      return;
    }

    const [sort, direction] = this.value.split("_");
    currentUrl.searchParams.set("sort", sort);
    currentUrl.searchParams.set("direction", direction);

    goTo(currentUrl.toString());
  });
});

const bttButton = document.querySelector(".btt-button");

  if (bttButton) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 300) {
        bttButton.classList.add("show");
      } else {
        bttButton.classList.remove("show");
      }
    });

    // Smooth scroll to top
    bttButton.addEventListener("click", function (e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    });
  }
