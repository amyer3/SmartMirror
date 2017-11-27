var currentArticle = -1,
    list=[],
    $ = require("jquery");

function getNews(){
    $.get(
        "https://newsapi.org/v1/articles?source=bbc-news&apiKey=d74b51d7710b45009dbb8e22bb21f0ec",
        function show(json) {
            for (let x = 0; x < json.articles.length; x++){
                list[x] = json.articles[x];
            }
            setIntervalX(post, 3000, list.length+1);
        }
    );
}

function post(){
    if (currentArticle < list.length-1){
        currentArticle++;
        $('#newsJQ').text(list[currentArticle].title);
        //$('#newsDesc').text(list[currentArticle].description);
    } else {
        currentArticle = -1;
        getNews();
    }
}

window.onload= getNews();

function setIntervalX(callback, delay, repetitions) {
    var x = 0;
    var intervalID = setInterval(function () {
        callback();

        if (++x === repetitions){
            window.clearInterval(intervalID);
        }

    }, delay);
}