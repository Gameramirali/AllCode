function addTag() {
    var nametag = document.getElementById("tagName").value;

    var tagnew = document.createElement(nametag);

    tagnew.textContent = "This is a " + nametag + " tag";

    document.body.appendChild(tagnew);
}