window.addEventListener("scroll", function () {
    let navScroll = document.getElementById("nav");
    navScroll.classList.toggle("fixed", window.scrollY > 5);
});

function navBack() {
    let nav = document.getElementById('nav').classList.toggle("change");
}