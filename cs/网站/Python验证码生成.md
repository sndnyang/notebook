Title: Python验证码生成  
Slug: python-validate-code-generatation  
Date: 2017-09-09 18:00:55  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code
Tags: python, 网站, web   
Category: web开发   
Summary: Python如何生成简单、基本的验证码图片  
  
[TOC]

# python后端

## call

    code_img, strs = create_validate_code()
    session['code_text'] = strs
    buf = StringIO.StringIO()
    code_img.save(buf, 'JPEG', quality=70)

    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

## implement

函数create_validate_code代码见[validation.py](https://github.com/sndnyang/zhimind/blob/master/wsgi/mindmap/validation.py)，不太看得懂

## 渲染

# 前端

## js

    document.getElementById("vericode")
            .setAttribute('src','/verifycode?random='+Math.random());

## html

    <div class="form-group">
        <label for="form-code">验证码
        <a href="#"><img onclick="this.setAttribute('src','/verifycode?random='+Math.random())" src="/verifycode" title="点击重新获取" /></a></label>
        <input id="code" name="code" type="text" value="">
    </div> 
