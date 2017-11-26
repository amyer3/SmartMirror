(function () {
    function checkTime(i) {return ( i < 10) ? "0" + i : i;}
    function hourFormat(i){return (i > 12) ? i-12 : i;}
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