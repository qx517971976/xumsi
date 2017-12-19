#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def sayHi(name, age):
    address = "Beijing"
    print "My name is %s,I am %s years old." % (name, age)
    return "hello world"

if sayHi("Msi", 22) == "hello world":
    print "wonderful!"
