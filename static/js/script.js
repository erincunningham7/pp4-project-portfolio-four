// const editButtons = document.getElementsByClassName("btn-edit");
// const advertText = document.getElementById("advert_text");
// const advertForm = document.getElementById("AdvertForm");
// const submitButton = document.getElementById("submitButton");

// /*
// * Initializes edit functionality for the edit buttons
// */
// for (let button of editButtons) {
//     button.addEventListener("click", (e) => {
//       let advertId = e.target.getAttribute("ad_id");
//       let advertContent = document.getElementById(`<int:ad_id>/${advertId}`).innerText;
//       advertText.value = advertContent;
//       submitButton.innerText = "Update";
//       commentForm.setAttribute("action", `edit_ad/${advertId}`);
//     });
//   }