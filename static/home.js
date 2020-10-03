const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.navlinks');
    const navLinks = document.querySelectorAll('.navlinks li');



    burger.addEventListener('click',() => {
        nav.classList.toggle('nav-active');
    });

   console.log(navLinks)

 }

navSlide();
