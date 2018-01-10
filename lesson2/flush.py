#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

f = file('ceshi', 'a')

for i in  range(15, 31):
    f.write('the %s loops\n'% i)
    time.sleep(1)
#    f.flush

f.close()
