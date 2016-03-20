#!/usr/bin/python

import urllib2
import re

index = "1"

while (index != ""):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + index
    content = urllib2.urlopen(url).read()
    print content
    m = re.findall(".*?([0-9]*)$", content)
    index = m[0]
    print index

