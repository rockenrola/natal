#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Usage:
# change SINGLE, SHUFFLED_FILE and Lusosms credentials

SINGLE='Bruno'
SHUFFLED_FILE = 'shuffled_20131204_181602.txt'
CONTACTS_FILE='nomes.csv'

import csv
from standalone_auxfunctions import *

# create contacts dictionary
contactosdict={}
dictreader = csv.DictReader(open(CONTACTS_FILE, newline=''), delimiter=',', quotechar='"')
for line in dictreader:
    if not line['nomes'].strip().startswith("#"):
        #print(line['nomes'])
        contactosdict[line['nomes']]=line['telemovel']

# create sorted dictionary
sorteiodict={}
dictreader = csv.DictReader(open(SHUFFLED_FILE, newline=''), fieldnames=['pessoa','sorteado'],delimiter=',', quotechar='"')
for line in dictreader:
    sorteiodict[line['pessoa']]=line['sorteado']

checkcredit(1)

if SINGLE in sorteiodict:
    #print(contactosdict[SINGLE])
    #print(sorteiodict[SINGLE])
    sendsms(contactosdict[SINGLE], "Ola " + SINGLE + ". Saiu-lhe no sorteio: " +  sorteiodict[SINGLE] + ".")
