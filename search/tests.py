from django.test import TestCase

import re
file = open('Origin_text.txt', 'r', encoding='windows-1251')
f = file.read().split(".")
word = 'часы'
r = re.compile(".*часы")
newlist = list(filter(r.match, f)) # Read Note