#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import time

os.system('pip install bs4')
os.system('pip install google')
os.system('clear')
os.system('xdg-open https://m.youtube.com/channel/UC17ehoE84IzPzzipMddupSQ')

print ("\33[32;1m▄▀▀░ ▄▀▄ ▄▀▄ ▄▀▀░ █░░ █▀▀  Author: TegarXploit")
time.sleep(0.5)
print ("\33[33;1m█░▀▌ █░█ █░█ █░▀▌ █░▄ █▀▀  Youtube: CYTOM")
time.sleep(0.5)
print ("\33[31;1m▀▀▀░ ░▀░ ░▀░ ▀▀▀░ ▀▀▀ ▀▀▀")
time.sleep(0.5)
print ("\33[37;1mcontoh dork:\33[32;1minurl://admin/login.php")
time.sleep(0.5)
print ("\33[37;1m")
time.sleep(0.5)
from googlesearch import search
query = str(input('Search: '))
for URL in search(query=query):
    print(URL)



