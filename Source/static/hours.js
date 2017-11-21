(function () {
    function checkTime(i) {return ( i < 10) ? "0" + i : i;}
    function startTime() {
        let today = new Date();
        $('#clock').text(
            checkTime(today.getHours())
            + ":" +
            checkTime(today.getMinutes())
            + ":" +
            checkTime(today.getSeconds())
        );
        setTimeout(function () {startTime()}, 500);}
    startTime();
})();