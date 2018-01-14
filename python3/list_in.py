#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a=['jim', 'tom', 'lily', 'lilei', 'xiaoming']

while True:
    name = input('请报上你的名字:')
    if name in a:
        print('Congratulations')
        break
    else:
        print('nope')
