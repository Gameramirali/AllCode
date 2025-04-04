document.getElementById('countrySelect').addEventListener('change', ()=>{
    var cities = {
        Iran: ["Tehran", "Mashhad", "Isfahan"],
        Turkey: ["Istanbul", "Ankara", "Izmir"],
        US: ["New York", "Los Angeles", "Chicago"],
    };

    let selectedCountry = document.getElementById('countrySelect').value
    let selectedCity = document.getElementById('citySelect')

    selectedCity.innerHTML = '<option value="">Select a city...</option>'

    if (cities[selectedCountry]) {
        for (var city of cities[selectedCountry]) {
            var option = document.createElement('option')
            option.value=city
            option.textContent=city
            selectedCity.appendChild(option)
        }
    }
})