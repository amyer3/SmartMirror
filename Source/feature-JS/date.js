var $ = require("jquery");
(function getToday(){
    let date = new Date(),
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    $('#date').text(month[date.getMonth()]+" "+date.getDate());
    $('#day').text(days[date.getDay()]);
    setTimeout(function(){getToday()}, 84000);
})();