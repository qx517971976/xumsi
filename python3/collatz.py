#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def collatz(number):
    print(number) 
    if number == 1: 
        exit()  
    elif number % 2 == 1: 
        t=number*3+1  
        collatz(t)  
    else:
        t=number//2  
        collatz(t)  

try:  
    n=int(input('请输入一个正整数：'))
    collatz(n)
except RuntimeError:
    print('超出最大递归深度,请输入一个正整数')
except ValueError:
    print('不能输入字符串,请输入一个正整数')
