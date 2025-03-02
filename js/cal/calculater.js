function addToCalculator(value){
    document.getElementById("displayResult").value+=value;
}

function finilize(){
    document.getElementById("displayResult").value=eval(
        document.getElementById("displayResult").value
    );
}

function mathCalculater(f_name){
    let val=document.getElementById("displayResult").value
    document.getElementById("displayResult").value = Math[f_name](val)
}