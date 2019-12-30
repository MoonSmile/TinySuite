# -*- coding: utf-8 -*-


import base64
 
with open("D:\\git\\diagram.png", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('data:image/jpeg;base64,%s'%s)