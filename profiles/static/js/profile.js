/* jshint esversion: 6 */
/* global $ */

$(function () {
  const $country = $("#id_default_country");

  function syncCountryColor() {
    $country.toggleClass("country-selected", !!$country.val());
  }

  syncCountryColor();
  $country.on("change", syncCountryColor);
});