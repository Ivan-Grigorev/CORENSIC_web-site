window.onscroll = function() {hideButton()};

function hideButton() {
    if (document.body.scrollTop > 2900 || document.documentElement.scrollTop > 2900) {
        document.getElementById("btn-contact-us").style.display = "none";
    } else {
        document.getElementById("btn-contact-us").style.display = "block";
    }
}
