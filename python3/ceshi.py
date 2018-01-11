#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def collatz(number):  
    print(number)  
    if number == 1:  
        exit()  
    elif number % 2 == 1 :  
        t=number*3+1  
        collatz(t)  
    else:  
        t=number//2  
        collatz(t)  
  
if __name__=='__main__':  
    n=input('Enter number: ')  
    try:  
        n=int(n)  
        collatz(n)  
    except ValueError as verror:  
        print('ValueError: You need input digital.')
