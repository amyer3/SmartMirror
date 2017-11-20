(function getWeather(){
    const url ="http://api.wunderground.com/api/de2db4c3e5c2c626/geolookup/conditions/q/CA/San_Francisco.xml";
    $.get(
        url ,
        function(xml){
            $('#weather').text(
                $(xml).find('weather').text()+
                " "+
                $(xml).find('temp_f').text()+
                String.fromCharCode(176)
            );
        }
    );
    setTimeout(function(){getWeather()}, 900000);
})();