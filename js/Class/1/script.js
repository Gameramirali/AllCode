let citiesData = {
    tehran: {
        city: 'Tehran', temp: 12, weather: 'Sunny', humidity: 23, windSpeed: 32
    },
    shiraz: {
        city: 'Shiraz', temp: 22, weather: 'Sunny', humidity: 33, windSpeed: 30

    }
}

let searchBtn = document.getElementById('search');
let searchBar = document.querySelector('.search-bar')
searchBtn.addEventListener('click', function () {
    let searchBarValue = searchBar.value
    let mainCityData = citiesData[searchBarValue]
    console.log(mainCityData)
    setInterval(function () {
        document.querySelector('.weather').classList.remove('loading')
    }, 3000);
    document.querySelector(".city").innerHTML = `<h2 class="city">${mainCityData.city}</h2>`;
    document.querySelector(".temp").innerHTML = `<h1 class="temp">${mainCityData.temp}°C</h1>`;
    document.querySelector(".weather").innerHTML = `<div class="description">${mainCityData.weather}</div>`;
    document.querySelector(".humidity").innerHTML = `<div class="humidity">Humidity: ${mainCityData.humidity}%</div>`;
    document.querySelector(".windSpeed").innerHTML = `<div class="windSpeed">Wind Speed: ${mainCityData.windSpeed}km/h</div>`;
})