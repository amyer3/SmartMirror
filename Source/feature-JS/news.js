var currentArticle = -1,
    list=[],
    $ = require('jquery');
const url = "https://newsapi.org/v2/top-headlines?sources=bbc-news,techcrunch,the-new-york-times,the-washington-post&apiKey=d74b51d7710b45009dbb8e22bb21f0ec";


function getNews(){
    $.get(url, function show(json) {
            for (let x = 0; x < json.articles.length; x++){
                list[x] = json.articles[x];
            }
            setIntervalX(post, 5000, list.length+1);
        });
}

function post(){
    if (currentArticle < list.length-1){
        currentArticle++;
        $("#newsJQ").fadeOut(1000,function() {
            $(this).text(list[currentArticle].title);
        }).fadeIn(1000);
        //$('#newsJQ').text(list[currentArticle].title);
        //$('#newsDesc').text(list[currentArticle].description);
    } else {
        currentArticle = -1;
        getNews();
    }
}

window.onload= getNews();

function setIntervalX(callback, delay, repetitions) {
    let x = 0;
    let intervalID = setInterval(function () {
        callback();
        if (++x === repetitions){
            window.clearInterval(intervalID);
        }
    }, delay);
}