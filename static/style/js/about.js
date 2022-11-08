new Swiper('.swiper', {
    slidesPerView: 3,
    centeredSlides: true,
    spaceBetween: 30,

    pagination: {
        el: '.swiper-pagination',
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
})