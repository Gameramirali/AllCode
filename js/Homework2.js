// 1:
// var age=prompt('Enter your age> ')
// if (age>18){
//     console.log('You can login')
//     alert('You can login')
// }
// else{
//     console.log("You can't login")
//     alert("You can't login") 
// }

// 2:
// var number1=prompt('Enter your number1> ')
// var number2=prompt('Enter your number2> ')
// console.log(number1**number2)
// alert(number1**number2)

// 3:
// var minute=prompt('Enter a minute:')
// console.log(minute/60)
// alert(minute/60)

// function Even_odd(number){
//     if(number%2==1){
//         alert('Even')
//         console.log('Even')
//     }
//     else{
//         alert('Odd')
//         console.log('Odd')
//     }
// }


// var num1=Number(prompt('Enter the number: '))
// Even_odd(num1)


// var mytext = "sample text";
// console.log(typeof mytext);
// console.log(mytext.length);
// function validate(event) {
// if (event.target.value.length < 3) {
//     alert("خطا طول اسم باید حداقل سه کاراکتر باشد");
// }}


let input_pass=document.getElementById('input-pass')
function test(){
    if (input_pass.value.length<3){
        alert("You can't login")
    }
    else{
        alert("You can login")
    }
}