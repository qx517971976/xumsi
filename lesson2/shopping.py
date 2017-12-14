#!/usr/bin/env python
# -*- coding: UTF-8 -*-

products = ['car', 'phone', 'coffee', 'bag']
prices = [50000, 3000, 20, 200]

salary = int(raw_input("你的工资:"))
shopping_list = []

while True:
    print "在售的产品有:"
    
    for p in products:
        print p,prices[products.index(p)]

    option = raw_input("你想买什么:").strip()

    if len(option) == 0:continue
    if option in products:
        p_price = prices[ products.index(option) ]
        if salary > p_price :
            print 'adding %s into shopping list.' % option
            shopping_list.append(option)
            salary -= p_price
            print "your current balance:%s" % salary
            continue
        else:
            print "\033[33;1mSorry, you cannot afford to buy %s\033[0m " % option
            if salary < min(prices):
                print "穷，都买不起"
                break

