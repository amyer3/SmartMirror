var upArrow = String.fromCharCode(9650),
    downArrow = String.fromCharCode(9660),
    deg = String.fromCharCode(176),
    $= require("jquery");

(function getWeather(){
    const url ="http://api.wunderground.com/api/de2db4c3e5c2c626/geolookup/forecast10day/q/CA/San_Francisco.json";
    $.getJSON(
        url ,
        function(json){
            let high = json.forecast.simpleforecast.forecastday[0].high.fahrenheit,
                low = json.forecast.simpleforecast.forecastday[0].low.fahrenheit,
                cond = json.forecast.simpleforecast.forecastday[0].conditions;
            $('#high').text(upArrow+high+deg);
            $('#low').text(downArrow+low+deg);
            $('#weatherIcon').attr("src", setSVG(cond));


        }
    );
    setTimeout(function(){getWeather()}, 1800000);
})();

function setSVG(cond){
    let date = new Date().getHours();
    if (cond.includes("drizzle")){
        return "animated/sun-rain.svg";
    } else if (cond.includes("rain")){
        return "animated/heavy-rain.svg";
    } else if (cond.includes("snow")){
        return "animated/snow.svg";
    } else if (cond.includes("overcast")){
        if (date >= 6 && date <= 19){
            return "animated/cloudy-day-1.svg";
        } else {
            return "animated/cloudy-night-1.svg";
        }
    } else if(cond.includes("fog")){
        return "animated/cloudy.svg";
    } else if(cond.includes("thunder")){
        return "animated/thunder.svg";
    } else {
        if (date >= 4 && date <= 17){
            return "animated/day.svg";
        } else {
            return "animated/night.svg";
        }
    }
}