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
    setTimeout(function(){getWeather()}, 900000);
})();

function setSVG(cond){return null}