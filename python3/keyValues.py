#!/usr/bin/env python
# -*- coding: UTF-8 -*-

bir = {'jim':'2月', 'sam':'5月', 'lily':'12月'}
'''
while True:
    print('输入姓名得出生日')
    name = input()
    
    if name == '':
        print('请输入一个名字\n')
        continue
    elif name in bir:
        print('%s的生日是' % name + bir[name])
    else:
        print('抱歉，目前没有存入%s的生日\n' % name)
        body = input('请输入%s的生日已更新数据: ' % name)
        bir[name] = body
        print('%s的生日已更新到数据库!\n' % name) 
'''

'''
for i in bir.items():
    print(list(i))
'''

bir.setdefault('lly','over')

print(bir)




