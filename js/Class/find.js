// var users = [
//     {id:1, name:'ali',password : '12345', age:21},
//     {id:2, name:'amin',password : '12345', age:12},
//     {id:3, name:'nikan',password : '12345', age:13},
//     {id:4, name:'sara', password : '12345',age:25},
// ]

// var username=prompt('name:')
// var finding=users.find(function(user){
//     return user.name===username
// })

// if (finding===undefined){
//     console.error('user not founded')
// }else{
//     console.log('Your password:',finding.password)
// }


// var i = 10
// var timer=setInterval(function(){
//     if(i===0){
//         console.error('Game Over');
//         clearInterval(timer)
//     }
//     console.log(i)
//     i--
// },1000)

var minutes = Number(prompt('enter the minutes: '))
var secends = Number(prompt('enter the secends: '))

var timer = setInterval(function () {
    if (minutes === 0 && secends === 0) {
        alert('Finished timer')
        clearInterval(timer)
    }
    if (secends === 0) {
        minutes--;
        secends = 59
    }
    console.log(`${minutes}:${secends}`);
    secends--
}, 1000)