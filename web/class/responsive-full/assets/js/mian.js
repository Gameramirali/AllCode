function myclick(){
    var x = document.getElementById("mynav");
    if (x.className === "nav"){
        x.className += " responsive";
    }
    else{
        x.className = "nav";
    }
}


document.addEventListener('contextmenu', (e)=>{
    e.preventDefault()
})