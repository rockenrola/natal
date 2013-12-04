#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from random import shuffle
from time import localtime, strftime

#import cgi, cgitb
#cgitb.enable()
#print "Content-Type: text/html\n"

lista = []
FILE = open("nomes.txt", 'r')
for line in FILE.readlines():
    if not line.strip().startswith("#"):
        lista.append(line.strip())
FILE.close()

shuffle(lista)
shuffle(lista)
shuffle(lista)
shuffle(lista)
shuffle(lista)

# uncomment for debugging
#k = -1
#while k < len(lista) - 1:
#    print "%s -> %s" %(lista[k], lista[k+1])
#    k = k + 1

FILE = open("shuffled_%s.txt" %strftime("%Y_%m_%d_%H-%M_%S", localtime()), "w")
k = -1
while k < len(lista) - 1:
    FILE.writelines("%s,%s\n" %(lista[k], lista[k+1]))
    k = k + 1
FILE.close()
