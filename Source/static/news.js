var currentArticle = -1,
    list=[];

function getNews(){
    $.get(
        "https://newsapi.org/v1/articles?source=bbc-news&apiKey=d74b51d7710b45009dbb8e22bb21f0ec",
        function show(json) {
            console.log("Running");
            for (let x = 0; x < json.articles.length; x++){
                list.push(json.articles[x]);
            }
            setInterval(post, 5000);
        }
    );
}

function post(){
    if (currentArticle < list.length -1){
        currentArticle++
    } else {
        currentArticle = 0;
        getNews();
    }
    $('#newsJQ').text(list[currentArticle].title);
    $('#newsDesc').text(list[currentArticle].description);
    console.log(currentArticle)
}


window.onload= getNews();