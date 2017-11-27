#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Usage:
# create a file named nomes.csv with names and phone numbers separated by a comma. The first line should be "nomes,telemovel".
# Have an account in www.lusosms.com or changed the code to handle another site
# Run the script

from random import shuffle
import csv
from time import localtime, strftime
from datetime import date

INFILE_NAME='nomes.csv'
OUTFILE_NAME="shuffled_%s.txt" %strftime("%Y%m%d_%H%M%S", localtime())



from standalone_auxfunctions import *

contactosdict={}
lista=[]
dictreader = csv.DictReader(open(INFILE_NAME, newline=''), delimiter=',', quotechar='"')
for line in dictreader:
    if not line['nomes'].strip().startswith("#"):
        #print(line['nomes'])
        lista.append(line['nomes'])
        contactosdict[line['nomes']]=line['telemovel']

checkcredit(len(lista))

shuffle(lista)
shuffle(lista)
shuffle(lista)


listadict={}
k = -1;
while k<len(lista)-1:
    listadict[lista[k]] = lista[k+1]
    k=k+1

for pessoa in listadict:
  message = "Ola " + pessoa + ". Saiu-lhe no sorteio: " +  listadict[pessoa] + ". Feliz Natal " + str(date.today().year)
  print("message sent to: " + pessoa )
  #print(pessoa, ' - ', listadict[pessoa], ' - ', contactosdict[pessoa], message)
  sendsms(contactosdict[pessoa], message)
  #send_mail(contactosdict[pessoa], message, 'Natal ' + str(date.today().year))


OUTFILE = open(OUTFILE_NAME,"w")
k= -1;
while k<len(lista)-1:
	OUTFILE.writelines("%s,%s\n" %(lista[k],lista[k+1]))
	k=k+1
OUTFILE.close()

