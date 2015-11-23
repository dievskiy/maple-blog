#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: hello.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-14 21:19:56
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from app import create_app
from werkzeug.contrib.fixers import ProxyFix

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()