/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
    navToggle = document.getElementById('nav-toggle'),
    navClose = document.getElementById('nav-close')


/*=============== MENU SHOW ===============*/
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu')
    })
}

/*=============== MENU HIDDEN ===============*/
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu')
    })
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link');

const linkAction = () => {
    // When we click on each nav__link, we remove the show-menu
    navMenu.classList.remove('show-menu');
};

navLink.forEach(n => n.addEventListener('click', linkAction));

/*=============== CHANGE BACKGROUND HEADER ===============*/
const scrollHeader = () => {
    const header = document.getElementById('header');
    // When the scroll is greater than 50 viewport height, add the scroll-header class to the header tag
    this.scrollY >= 50 ? header.classList.add('bg-header')
                         : header.classList.remove('bg-header');
};
window.addEventListener('scroll', scrollHeader);


/*=============== TESTIMONIAL SWIPER ===============*/



/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

const scrollActive = () =>{
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight,
              sectionTop = current.offsetTop - 58,
              sectionId = current.getAttribute('id'),
              sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            sectionsClass.classList.add('active-link')
        }else{
            sectionsClass.classList.remove('active-link')
        }
    })
}

window.addEventListener('scroll', scrollActive)


/*=============== SHOW SCROLL UP ===============*/ 
const scrollUp = () => {
    const scrollUp = document.getElementById('scroll-up');
    if (scrollUp) {
        this.scrollY >= 350 
            ? scrollUp.classList.add('show-scroll')
            : scrollUp.classList.remove('show-scroll');
    }
};

window.addEventListener('scroll', scrollUp)

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px', 
    duration: 2500,
    delay: 00,
})

sr.reveal('.home__data, .footer__container, .footer__group')
sr.reveal('.home__img', {delay: 700, origin: 'bottom'})
sr.reveal(' .program__card, .pricing__card', {interval: 100})
sr.reveal('.choose__img', {origin: 'left'})
sr.reveal('.choose__content', {origin: 'right'})


/*=============== LOGO SCROLL =============== */
document.addEventListener("DOMContentLoaded", () => {
    const track = document.querySelector(".logos__track");
    const logos = Array.from(track.children);
  
    // Duplicate logos to ensure a seamless scroll effect
    logos.forEach(logo => {
      const clone = logo.cloneNode(true);
      track.appendChild(clone);
    });
  
    // Calculate the total width of all logos, including the duplicates
    const totalWidth = track.scrollWidth / 2; // Original width of one set
  
    // Set animation duration based on the total width
    const speed = 0.015; // Adjust this value to control speed (lower = slower)
    const duration1 = totalWidth * speed;
    track.style.animationDuration = `${duration1}s`;
  });
  
  








/*=============== EMAIL JS ===============*/
emailjs.init('TzLsx2oaRZgLZVBEv');

const contactForm = document.getElementById('contact-form'),
      contactMessage = document.getElementById('contact-message'),
      contactUser = document.getElementById('contact-user');

const sendEmail = (e) => {
    e.preventDefault();
    
    // Check if the email field is empty
    if (contactUser.value.trim() === '') {
        // Ensure error color class is added and success color class is removed
        contactMessage.classList.remove('color-green');
        contactMessage.classList.add('color-red');
        
        // Show error message
        contactMessage.textContent = 'You must enter your email.';

        // Remove message 3 sec
        setTimeout(() =>{
            contactMessage.textContent = ''
        }, 3000)
    } else{
        emailjs.sendForm('service_x2me7er', 'template_iiycugr', '#contact-form')
            .then(() => {
                contactMessage.classList.add('color-green');
                contactMessage.textContent = 'You registered successfully';

                // Remove message 3 sec
                setTimeout(() =>{
                    contactMessage.textContent = ''
                }, 3000)
            }, (error) =>{
                // 404 Error
                alert('Error', error)
            })
        
        // Clear input field
        contactUser.value = ''
    }
};

// Attach event listener to the form
contactForm.addEventListener('submit', sendEmail);

