#!/usr/bin/python
import string

######1
def translate(ch):
    if ch != '.' and ch != ' ' and ch != "'" and ch!= '(' and ch!= ')':
        return chr((ord(ch)-ord('a')+2) % (ord('z')-ord('a')+1) + ord('a'))
    else:
        return ch

cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
plain = "".join( [translate(ch) for ch in cipher] )
print plain
######

######2
table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print cipher.translate(table)
######

######solve
cipher2 = "http://www.pythonchallenge.com/pc/def/map.html"
print cipher2.translate(table)
