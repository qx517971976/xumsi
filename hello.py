#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from IPy import IP

#接收输入信息，输入格式如：192.168.0.0/24或192.168.0.1
ip_s = raw_input('Please input an IP or net-range: ')
ips = IP(ip_s)
fd
放到

if len(ips) > 1:											#IP数量大于1
    print('net: %s' % ips.net())							#输出网络地址
    print('netmask: %s' % ips.netmask())					#输出子网掩码
    print('broadcast: %s' % ips.broadcast())				#输出广播地址
    print('reverse address: %s' % ips.reverseNames()[0])	#输出地址反向解析
    print('subnet: %s' % len(ips))							#输出ip总数
else:
    print('reverse address: %s' % ips.reverseNames()[0])	

print('hexadecimal: %s' % ips.strHex())						#输出16进制地址
print('binary ip: %s' % ips.strBin())						#输出2进制地址
print('iptype: %s' % ips.iptype())							#输出地址类型，如PRIVATE、PUBLIC、LOOPBACK
