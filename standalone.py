#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Usage:
# create a file named nomes.csv with names and phone numbers separated by a comma. The first line should be "nomes,telemovel".
# Have an account in www.lusosms.com or changed the code to handle another site
# Run the script

from random import shuffle
import csv
from time import localtime, strftime
import http.client

INFILE_NAME='nomes.csv'
OUTFILE_NAME="shuffled_%s.txt" %strftime("%Y%m%d_%H%M%S", localtime())
LUSOSMS_USER="CHANGE USER"
LUSOSMS_PASS="CHANGE PASS"
LUSOSMS_NUMBER="CHANGE NUMBER"


def checkcredit(listsize):
    gettext="/ver_credito_get.php?username=" + LUSOSMS_USER + "&password=" + LUSOSMS_PASS
    gettext = gettext.replace(" ","+")
    #print(gettext)
    conn = http.client.HTTPConnection("www.lusosms.com")
    conn.request("GET", gettext)
    r1 = conn.getresponse()
    data1 = r1.read()
    if (float(data1.decode("utf-8")) < listsize):
        print(data1)
        print('Not enough credits')
        exit()
    conn.close()

#function for sms
def sendsms(tlmdestino, texto):
    gettext="/enviar_sms_get.php?username=" + LUSOSMS_USER + "&password=" + \
            LUSOSMS_PASS + "&origem=" + LUSOSMS_NUMBER + "&destino=" + tlmdestino + "&mensagem=" + texto
    gettext = gettext.replace(" ","+")
    #print(gettext)
    conn = http.client.HTTPConnection("www.lusosms.com")
    conn.request("GET", gettext)
    r1 = conn.getresponse()
    data1 = r1.read()
    if(data1 != b'mensagem_enviada'):
        #print(data1)
        exit()
    conn.close()


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
  #print(pessoa, ' - ', listadict[pessoa], ' - ', contactosdict[pessoa])
  sendsms(contactosdict[pessoa], "Ola " + pessoa + ". Saiu-lhe no sorteio: " +  listadict[pessoa] + ".")


#pessoa='São'
#sendsms(listadict[pessoa], "A " + pessoa + " saiu " +  listadict[pessoa])



OUTFILE = open(OUTFILE_NAME,"w")
k= -1;
while k<len(lista)-1:
	OUTFILE.writelines("%s,%s\n" %(lista[k],lista[k+1]))
	k=k+1
OUTFILE.close()

