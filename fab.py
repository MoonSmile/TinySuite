# -*- coding: utf-8 -*-

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b ,a+b
        n = n + 1
        
for f in fab(5):
    print(f)