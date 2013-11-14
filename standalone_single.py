#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Usage:
# change SINGLE, SHUFFLED_FILE and Lusosms credentials

SINGLE='Nuno'
#SHUFFLED_FILE = 'shuffled_20121204_212803.txt'
SHUFFLED_FILE = 'shuffled_20121204_142354.txt'
import http.client, csv


CONTACTS_FILE='nomes.csv'
LUSOSMS_USER=""
LUSOSMS_PASS=""
LUSOSMS_NUMBER=""

#function for sms
def sendsms(tlmdestino, texto):
    gettext="/enviar_sms_get.php?username=" + LUSOSMS_USER + "&password=" + \
            LUSOSMS_PASS + "&origem=" + LUSOSMS_NUMBER + "&destino=" + tlmdestino + "&mensagem=" + texto
    gettext = gettext.replace(" ","+")
    print(gettext)
    conn = http.client.HTTPConnection("www.lusosms.com")
    conn.request("GET", gettext)
    r1 = conn.getresponse()
    data1 = r1.read()
    print(data1)
    if(data1 != b'mensagem_enviada'):
        #print(data1)
        exit()
    conn.close()


contactosdict={}
dictreader = csv.DictReader(open(CONTACTS_FILE, newline=''), delimiter=',', quotechar='"')
for line in dictreader:
    contactosdict[line['nomes']]=line['telemovel']


sorteiodict={}
dictreader = csv.DictReader(open(SHUFFLED_FILE, newline=''), fieldnames=['pessoa','sorteado'],delimiter=',', quotechar='"')
for line in dictreader:
    sorteiodict[line['pessoa']]=line['sorteado']


if SINGLE in sorteiodict:
    print(contactosdict[SINGLE])
    #print(sorteiodict[SINGLE])
    sendsms(contactosdict[SINGLE], "Ola " + SINGLE + ". Saiu-lhe no sorteio: " +  sorteiodict[SINGLE] + ".")
