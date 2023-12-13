document.addEventListener('contextmenu', event => event.preventDefault());

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

function smallerBoxClick(event) {
    event.stopPropagation();
}

const container = document.querySelector(".container"),
    pwShowHide = document.querySelectorAll(".showHidePw"),
    pwFields = document.querySelectorAll(".password"),
    signUp = document.querySelector(".signup-link"),
    fsignUp = document.querySelector(".fsignup-link"),
    login = document.querySelector(".login-link");
forgot = document.querySelector(".forgot-link");

//   js code to show/hide password and change icon
pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        pwFields.forEach(pwField => {
            if (pwField.type === "password") {
                pwField.type = "text";

                pwShowHide.forEach(icon => {
                    icon.classList.replace("uil-eye-slash", "uil-eye");
                })
            } else {
                pwField.type = "password";

                pwShowHide.forEach(icon => {
                    icon.classList.replace("uil-eye", "uil-eye-slash");
                })
            }
        })
    })
})

function dsignup() {
    document.getElementById("myForm").style.display = "block";
    container.classList.add("active");
}
// js code to appear signup and login form
signUp.addEventListener("click", () => {
    container.classList.add("active");
});
fsignUp.addEventListener("click", () => {
    container.classList.remove("active1");
    container.classList.add("active");
});
login.addEventListener("click", () => {
    container.classList.remove("active");
});

forgot.addEventListener("click", () => {
    container.classList.add("active1");
});


// variables
var accordionBtn = document.querySelectorAll('.accordionTitle');
var allTexts = document.querySelectorAll('.text');
var accIcon = document.querySelectorAll('.accIcon');

// event listener
accordionBtn.forEach(function (el) {
    el.addEventListener('click', toggleAccordion)
});

// function
function toggleAccordion(el) {
    var targetText = el.currentTarget.nextElementSibling.classList;
    var targetAccIcon = el.currentTarget.children[0];
    var target = el.currentTarget;

    if (targetText.contains('show')) {
        targetText.remove('show');
        targetAccIcon.classList.remove('anime');
        target.classList.remove('accordionTitleActive');
    } else {
        accordionBtn.forEach(function (el) {
            el.classList.remove('accordionTitleActive');

            allTexts.forEach(function (el) {
                el.classList.remove('show');
            })

            accIcon.forEach(function (el) {
                el.classList.remove('anime');
            })

        })

        targetText.add('show');
        target.classList.add('accordionTitleActive');
        targetAccIcon.classList.add('anime');
    }
}