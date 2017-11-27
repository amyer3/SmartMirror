var $ = require("jquery");
(function () {
    function checkTime(i) {return ( i < 10) ? "0" + i : i;}
    function hourFormat(i){
        if (i > 12){
            return i-12
        } else if (i === 0){
            return 12
        } else {
            return i
        }

    }
    function amPM(i) {return (i < 12) ? "AM" : "PM"}
    function startTime() {
        let today = new Date();
        $('#clock').text(
            hourFormat(today.getHours())
            + ":" +
            checkTime(today.getMinutes())
            + " " +
            amPM(today.getHours())
        );
        setTimeout(function () {startTime()}, 500);}
    startTime();
})();