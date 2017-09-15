Title: python-logging模块配置多个logger  
Slug: python-flask-logging-logger  
Date: 2017-09-09 15:32:25  
Author: sndnyang (sndnyangd@gmail.com)  
Type: code
Tags: python, flask, 日志   
Category: python   
Summary: python logging 和 flask 如何弄多个 logger 写不同日志文件 
  
[TOC]

# flask app.logger

    log_file_name = os.path.join(
        os.environ.get('OPENSHIFT_PYTHON_LOG_DIR', '.'),
        'app.log')

    handler = logging.FileHandler(log_file_name, mode='a')
    handler.setLevel(logging.INFO)
    fmt = "%(asctime)s\t%(message)s"
    # 实例化formatter
    formatter = logging.Formatter(fmt)
    # 为handler添加formatter
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

# 其他logger

    logger = logging.getLogger('selfname')
    fmter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    log_file_name = os.path.join(os.environ.get('OPENSHIFT_PYTHON_LOG_DIR', '.'),
                                 'filename.log')
    hdlr = logging.FileHandler(log_file_name, mode='a')
    hdlr.setLevel(logging.INFO)
    hdlr.setFormatter(fmter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)