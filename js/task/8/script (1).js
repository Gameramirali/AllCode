// let h1Element = document.getElementById("title");
// console.log(h1Element.className);
// console.log(h1Element.getAttribute('class'));


// let usernameInput = document.getElementById("input");
// usernameInput.setAttribute('location', 'input field');
// console.log(usernameInput.getAttribute('location'));
// usernameInput.location = "blalalala"
// console.log(usernameInput.location);


// let usernameInput = document.getElementById("input");
// console.log(usernameInput.hasAttribute('href'));

// function removeAttrHandler() {
//     usernameInput.removeAttribute('placeholder');
//     console.log(usernameInput.getAttribute('placeholder'));
// }

// let btn = document.getElementById("btn");
// function showLog(){
//     console.log("Clicked!")
// }

// btn.onclick = showLog;

// let usernameInput = document.getElementById("username");
// usernameInput.addEventListener("keydown", function(event) {
//     console.log(event.key);
//     if (event.key === "Enter") {
//         console.log("You pressed Enter!");
//     }
// })

// let loginForm = document.getElementsByTagName("form")[0];
// loginForm.addEventListener("submit", function(event) {
//     event.preventDefault(); // Prevent the form from submitting
// })

let locationElem = document.querySelector("#location");
let keyElem = document.querySelector("#key");
document.body.addEventListener("keydown", function(event) {
    starter.style.display = "none"
    ascii.style.display = "flex"
    locationElem.innerHTML = event.location;
    keyElem.innerHTML = event.key;
})


const key=document.querySelector('#key').value
const location=document.querySelector('#location').value
const witch=document.querySelector('#witch').value
const code=document.querySelector('#code').value

