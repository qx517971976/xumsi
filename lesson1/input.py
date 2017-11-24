#!/usr/bin/env python

import tab

for i in range(3):
    name = raw_input('What is your name?').strip()
    if len(name) == 0:
        continue
    break
