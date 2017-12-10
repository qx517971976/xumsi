#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import time
import fileinput
for line in fileinput.input("ceshi", inplace=1):
    line = line.replace("hehe","hello")
    print line,
