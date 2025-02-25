

function Submit(){
    var num=Number(0)
    let MyResult=document.getElementById('Result').value
    for (let i = 0; i < MyResult.length; i++) {
        num=Number(num)+Number(MyResult[i])
    }
    alert(num)
}