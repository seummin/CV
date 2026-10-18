"use strict";

const printButton = document.querySelector(".print-button");
if (printButton) {
  printButton.hidden = false;
  printButton.addEventListener("click", () => window.print());
}
