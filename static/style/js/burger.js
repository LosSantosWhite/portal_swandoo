const active = "burger__active";
const menuBurgerItems = document.querySelector(".header-nav__items");
const menuHeader = document.querySelector(".header_nav");


function mainMenu(id) {
    console.log('Захожу в функцию')
    const element = document.getElementById(id)
    console.log(element.classList)

    element.addEventListener('click', (e) => {
        console.log('Захожу в ивентлистенер')
        element.classList.toggle(active);
        menuBurgerItems.classList.toggle('header-active');
        console.log('Активирова2н')

    })
}

console.log('Активирую..')
mainMenu("burgerMenu")