#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tab

#name = raw_input('What is your name?')
#age = int(raw_input('How old are you?'))

"""
for i in range(3):
    name = raw_input('What is your name?').strip()
    if len(name) == 0:
        continue
    break
"""

"""
if age <= 18:
    print "你太年轻了"
else:
    print "我叫%s，今年%d岁" %(name,age)
"""

while True:
    name = raw_input('What is your name?').strip()
    age = raw_input('How old are you?')
    if (len(name) == 0 or len(age) == 0):
        continue
    else:
        print "我叫%s" % name
        print "今年%s岁" % age
    break
