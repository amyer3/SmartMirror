(function getToday(){
    var date = new Date(),
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        $('#date').text(
            days[date.getDay()] +", "+month[date.getMonth()]+" "+date.getDate()+", "+date.getFullYear()
        );
    setTimeout(function(){getToday()}, 84000);
})();