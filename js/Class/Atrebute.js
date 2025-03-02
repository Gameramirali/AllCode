// let MyDiv=document.getElementById('MyDiv').childNodes[1]

// console.log(MyDiv.type)
// console.log(MyDiv.getAttribute("test"))
// MyDiv.setAttribute("new-atr","my-atr")
// MyDiv.setAttribute("new-atr2","my-atr2")

// console.log(MyDiv.value)
// MyDiv.value="newval"
// console.log(MyDiv.value)
// MyDiv.setAttribute("value","newvalue2")
// console.log(MyDiv.value)
// console.log(MyDiv.checked)


let div_body=document.createElement("div");
div_body.setAttribute("style","background-color:red; display:block;")
let ul=div_body.appendChild(document.createElement("ul"))
let n1=ul.appendChild(document.createElement('li'))
n1.appendChild(document.createTextNode('n1'))
let n2=ul.appendChild(document.createElement('li'))
n2.appendChild(document.createTextNode('n2'))
let a=ul.appendChild(document.createElement('a'))
a.appendChild(document.createTextNode('link'))
document.body.append(div_body)
// 

// let MyDiv=document.getElementsByClassName("new-element")[0];
// let newelem=document.createElement("ul")
// newelem.className="my-list"
// MyDiv.append(newelem)

// function getPlace(){
//     let myLi=document.createElement("li")
//     myLi.innerHTML="<strong>hello world</strong>"
//     newelem.append(myLi)
//     setTimeout(function(){
//         myLi.remove();
//     },2000)
// }