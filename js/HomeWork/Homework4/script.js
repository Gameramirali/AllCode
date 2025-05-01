// Variables
const ConvertBtn = document.querySelector('#convertButton'),
      ResetBtn = document.querySelector('#resetButton'),
      ChangeBtn = document.querySelector('#changeButton'),
      Converter = document.getElementById('converter');
let placeHolder = '°C';

// Event Listener
EventListener();
function EventListener() {
    ConvertBtn.addEventListener('click', ConvertFunc);
    ResetBtn.addEventListener('click', ResetFunc);
    ChangeBtn.addEventListener('click', ChangeFunc);
}

// Functions
// Convert Button Function
function ConvertFunc() {
    if (Converter.value === "" || isNaN(Converter.value)) {
        alert("Please enter a valid number!");
        return; 
    }
    if (placeHolder === '°C') {
        Converter.value = (parseFloat(Converter.value) * 1.8 + 32).toFixed(2);
    } else {
        Converter.value = ((parseFloat(Converter.value) - 32) / 1.8).toFixed(2);
    }
}

// Reset Button Function
function ResetFunc() {
    Converter.value = "";
}

// Change Button Function
function ChangeFunc() {
    if (placeHolder === '°C') {
        placeHolder = '°F';
        Converter.placeholder = placeHolder;
    } else {
        placeHolder = '°C';
        Converter.placeholder = placeHolder;
    }
}
// End of File