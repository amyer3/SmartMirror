var upArrow = String.fromCharCode(9650),
    downArrow = String.fromCharCode(9660),
    deg = String.fromCharCode(176),
    $ = require("jquery");

(function getWeather(){
    const url ="http://api.wunderground.com/api/de2db4c3e5c2c626/geolookup/forecast10day/q/CA/San_Francisco.json";
    $.getJSON(
        url ,
        function(json){
            let high = json.forecast.simpleforecast.forecastday[0].high.fahrenheit,
                low = json.forecast.simpleforecast.forecastday[0].low.fahrenheit,
                cond = json.forecast.simpleforecast.forecastday[0].conditions;
            $('#wStatus').text(upArrow+high+deg+" | " + low + deg+downArrow)
            setSVG(cond);
        }
    );
    setTimeout(function(){getWeather()}, 1800000);
})();

function setSVG(cond){
    let date = new Date().getHours()
    if (cond.includes("drizzle")){
        $('#weatherIcon').attr("src", "animated/sun-rain.svg")
    } else if (cond.includes("rain")){
        $('#weatherIcon').attr("src", "animated/heavy-rain.svg")
    } else if (cond.includes("snow")){
        $('#weatherIcon').attr("src", "animated/snow.svg")
    } else if (cond.includes("overcast")){
        if (date >= 6 && date <= 19){
            $('#weatherIcon').attr("src", "animated/cloudy-day-1.svg")
        } else {
            $('#weatherIcon').attr("src", "animated/cloudy-night-1.svg")
        }
    } else if(cond.includes("fog")){
        $('#weatherIcon').attr("src", "animated/cloudy.svg")
    } else if(cond.includes("thunder")){
        $('#weatherIcon').attr("src", "animated/thunder.svg")
    } else {
        if (date >= 4 && date <= 17){
            $('#weatherIcon').attr("src", "animated/day.svg")
        } else {
            $('#weatherIcon').attr("src", "animated/night.svg")
        }
    }
}