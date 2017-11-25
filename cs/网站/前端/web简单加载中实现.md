Title: web简单进度条\加载中实现  
slug: web-simple-loader  
tags: web, html, css, js 
summary: web简单进度条\加载中实现及调用, loader, loading
Date: 2017-05-30 13:27:22
Type: code

# js

## call

    $("#loadingDiv").remove();
    var loadingDiv = createLoadingDiv('想写什么写什么')                    
    //呈现loading效果
    $("#learning>.container-fluid").append(loadingDiv);

## implement

    function createLoadingDiv(prompt) {
        var _PageWidth = document.documentElement.clientWidth,
                _PageHeight = document.documentElement.clientHeight,
                _LoadingTop = _PageHeight / 2,
                _LoadingLeft = _PageWidth > 215 ? (_PageWidth - 215) / 2 : 0,
                _LoadingHtml = $('<div></div>');
            _LoadingHtml.attr("id", "loadingDiv");
            _LoadingHtml.html("<p>"+prompt+"</p>");
            return _LoadingHtml
    }

# html

    <script src="//www.zhimind.com/static/js/global.js" type="text/javascript"></script>
    <link href="//www.zhimind.com/static/css/loader.css" rel="stylesheet" media="screen" type="text/css"/>

# css


    #loadingDiv {
        position: fixed;
        cursor1: wait;
        left: 0px;
        top: 0px;
        width: 100%;
        height: 100%; 
        left: 0px;
        top: 0px;
        background-color: transparent;
        background: url(/static/img/loading.gif) 50% 50% no-repeat; 
        z-index: 2;
    }

    #loadingDiv p {
        position: fixed;
        left: 52%;
        top: 49%;
    }
