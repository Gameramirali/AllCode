function datavalidation() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var password2 = document.getElementById("password2").value;
    var error_message = document.getElementById("error_message");
    var text;
    error_message.style.padding = "10px";
    if (name.length < 5) {
        text = "Please Enter valid Name";
        error_message.innerHTML = text;
        return false;
    }
    if (email.indexOf("@") == -1 || email.length < 6) {
        text = "Please Enter valid Email";
        error_message.innerHTML = text;
        return false;
    }
    if (password.length < 8) {
        text = "Please Enter Correct Password";
        error_message.innerHTML = text;
        return false;
    }
    if (password2 != password) {
        text = "Please Enter Correct Password";
        error_message.innerHTML = text;
        return false;
    }
    alert("Form Submitted Successfully!");
    return true;
}