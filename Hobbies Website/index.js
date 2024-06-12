//IMAGE SLIDER

const slide = document.querySelectorAll(".slides img");
let slideIndex = 0;
let intervalId = null;

document.addEventListener("DOMContentLoaded", initializeSlider);

function initializeSlider(){

    if(slide.length > 0) {
        slide[slideIndex].classList.add("displaySlide");
        intervalId = setInterval(nextSlide, 5000);
    }

}

function showSlide(index) {
    slide.forEach(slide => {
        slide.classList.remove("displaySlide");
    });
    slide[slideIndex].classList.add("displaySlide");
}

function prevSlide(){

}

function nextSlide(){
    slideIndex++;
    showSlide(slideIndex);
}