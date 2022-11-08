const active = "burger__active";
const menuBurgerItems = document.querySelector(".header-nav__items");
const menuHeader = document.querySelector(".header_nav");
const burgerMenu = document.getElementById("burgerMenu")

function mainMenu(id) {
    const element = document.getElementById(id)

    element.addEventListener('click', (e) => {
        element.classList.toggle(active);
        burgerMenu.classList.toggle("green")
        menuBurgerItems.classList.toggle('header-active');
    })
}


mainMenu("burgerMenu")