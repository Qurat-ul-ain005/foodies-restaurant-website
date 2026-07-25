// View Menu Button

let menuButton = document.getElementById("menuBtn");

// Menu Section

let menuSection = document.getElementById("menu");

// Button Click

menuButton.addEventListener("click", function(){

    menuSection.scrollIntoView({
        behavior: "smooth"
    });

});

// Book Table Button

let bookButton = document.getElementById("bookBtn");

// Reservation Section

let reservationSection = document.getElementById("reservation");

// Button Click

bookButton.addEventListener("click", function(){

    reservationSection.scrollIntoView({
        behavior: "smooth"
    });

});

// Scroll To Top Button

let topButton = document.getElementById("topBtn");

// Button Show/Hide

window.addEventListener("scroll", function(){

    if(window.scrollY > 300){

        topButton.style.display = "block";

    }

    else{

        topButton.style.display = "none";

    }

});

// Scroll to Top

topButton.addEventListener("click", function(){

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

});

// Hamburger Menu

let menuIcon = document.getElementById("menuIcon");
let navLinks = document.getElementById("navLinks");

menuIcon.addEventListener("click", function(){

    navLinks.classList.toggle("show");

});
console.log("Filter JS Loaded");
const filterButtons = document.querySelectorAll(".filter-buttons button");
const cards = document.querySelectorAll(".card");

filterButtons.forEach(button => {
    button.addEventListener("click", function () {

        const filter = this.getAttribute("data-filter");

        filterButtons.forEach(btn => btn.classList.remove("active"));
        this.classList.add("active");

        cards.forEach(card => {

            const category = card.getAttribute("data-category");

            if (filter === "All" || category === filter) {
                card.style.display = "";
            } else {
                card.style.display = "none";
            }

        });

    });
});