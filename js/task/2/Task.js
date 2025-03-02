// for(var i=1;i<101;i++){
//     if (i%2==0){
//         console.log(i);
//     }
// }

// var a='AmirAli Pourbabaeii'

// for(i=0;i<a.length;i++){
//     console.log(i,a[i]);
// }

var num1=[]

function addToCalculator(value){
    document.getElementById("displayResult").value+=value;
    num1.push(value)
}
function reset() {
    alert('hello');
}

function finilize(){
    console.log(num1)
    var sum=num1.reduce((acc,curr)=>acc+curr,0);
    document.getElementById("displayResult").value=sum/num1.length;
}

