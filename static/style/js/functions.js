function showMore() {
  const elementBlock = document.getElementById('hideSpec');
  if (elementBlock.style.opacity === "0") {
    elementBlock.style.opacity = "1";
    elementBlock.style.height = "auto";
  } else {
    elementBlock.style.opacity = "0";
    elementBlock.style.height = "0";
  }
}


const defaultMenu = document.querySelectorAll("#mainMenu")

defaultMenu.addEventListener("scroll", e => {

})
