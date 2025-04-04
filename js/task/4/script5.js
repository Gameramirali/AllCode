
let username = document.getElementsByClassName('username')[0];
let password = document.getElementsByClassName('password')[0];
let modal = document.getElementsByClassName('modal')[0];
let usernameMessage = document.getElementsByClassName('username-message')[0];
let passwordMessage = document.getElementsByClassName('password-message')[0];

username.addEventListener('input', function() {
    if (username.value.length < 12) {
        usernameMessage.textContent = 'Username must be at least 12 characters long';
        usernameMessage.className = 'username-message error';
    } else {
        usernameMessage.textContent = 'Username is valid';
        usernameMessage.className = 'username-message success';
    }
});

password.addEventListener('input', function() {
    if (password.value.length < 8) {
        passwordMessage.textContent = 'Password must be at least 8 characters long';
        passwordMessage.className = 'password-message error';
    } else {
        passwordMessage.textContent = 'Password is valid';
        passwordMessage.className = 'password-message success';
    }
});

function dataValidation() {
    let usernameValue = username.value;
    let passwordValue = password.value;
    if (usernameValue.length < 12 || passwordValue.length < 8) {
        modal.style.display = 'inline';
        modal.style.backgroundColor = 'red';
        modal.innerHTML = 'Invalid username or password';
    } else {
        modal.style.display = 'inline';
        modal.style.backgroundColor = 'green';
        modal.innerHTML = 'Valid username and password';
    }
    setTimeout(() => {
        modal.style.display = 'none';
    }, 3000);
}