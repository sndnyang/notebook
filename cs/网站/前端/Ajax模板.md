Title: Ajax模板  
Slug: ajax-template  
Date: 2017-09-06 17:38:32  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code
Tags: jquery, ajax, web   
Category: web开发   
Summary: 用JQuery的ajax给服务器传数据的模板代码  
  
[TOC]

# JS

    $.ajax({  
        type: "post", //请求方式  
        url: "getResearchProgress", //发送请求地址  
        timeout: 30000,//超时时间：30秒
        contentType: 'application/json',
        dataType: "json",
        data: JSON.stringify({"url": url}),
        //请求成功后的回调函数 data为json格式  
        success:function(data){
            if (data.error) {
                window.clearInterval(timerId);
                alert(data.error);
                return;
            }
            
        },  
        //请求出错的处理  
        error: function(){  
            alert("请求出错");  
        }
    });  
