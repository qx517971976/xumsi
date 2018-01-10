#!/usr/bin/env python
# -*- coding: UTF-8 -*-

while True:
    print('Who are you?')
    name = input()
    if name != 'jim':
        continue
    while True:
        print('hello,jim.what is the password?')
        password = input()
        if password == '111111':
            break
    break
print('Access granted.')
