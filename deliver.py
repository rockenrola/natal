#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import cgi
import cgitb
cgitb.enable()

import csv
from auxfunctions import *

# inicio do programa
ficheiro = 'deliver.txt'
script = "deliver.py"
dictionary ={}
header()
try: 
	FILE = open(ficheiro,'rw')
	reader = csv.reader(FILE)
	for line in reader:
		dictionary[line[0]] = line[1]
	FILE.close()
except:
	print "Ficheiro nao existe ou nao é possivel abrir"
	footer()
	exit()

form = cgi.FieldStorage()
#print form
if form.has_key("nome"):
#        if form.getvalue("ecran_CB") or "email_CB" not in form or "sms_CB" not in form:
	if not form.has_key("ecran_CB") and not form.has_key("email_CB") and not form.has_key("sms_CB"):
		espaco()
	       	print """Não há nada selecionado """
	elif form.has_key("email_CB") and invalidemail(form["email"].value):
		print "email invalido"
	elif form.has_key("sms_CB") and invalidphone(form["sms"].value):
		print "telemovel invalido"
	else:
		# extrat the name from the dictionary
		try: 
			FILE = open(ficheiro,"w")
                	pessoa = form["nome"].value
                	sorteado = dictionary.pop(form["nome"].value)
			for key, value in dictionary.iteritems():
				FILE.writelines(key + "," + value+"\n")
			FILE.close()
		except: 
			print "Erro ao abrir ficheiro"
			footer()
			exit()
		# print on the monitor
	        if form.getvalue("ecran_CB"):
			espaco()
			print "<p>À pessoa <b>" + pessoa + "</b> saiu-lhe na sorte a pessoa <b>" + sorteado + ".</b></p>"
		# send an email
        	if form.getvalue("email_CB"):
                	print "Email enviado para " + form["email"].value
	                espaco()
        	        sendemail(form["email"].value, "A " + pessoa + " saiu " +  sorteado)

		# send an sms
	        if form.getvalue("sms_CB"):
        	        print "Enviado para: " + form["sms"].value
                	espaco()               
	                sendsms(form["sms"].value, "A " + pessoa + " saiu " +  sorteado)
		# return
	espaco()
	print """<a href="%s">Voltar ao início</a>""" %script
        espaco()

else:
	lista=dictionary.keys()
	lista.sort()
	print "<h1>Escolha o seu nome e carregue submeter</h1>"
	print "<p>Apenas estará disponível uma vez sendo apagado depois de visto.</p>"
	print "<p>Em caso de engano será necessário recomeçar tudo.</p>"
	print """<FORM ACTION="%s" method="post">""" %script
#	print """<FORM ACTION="%s" method="get">""" %script
	print """<SELECT NAME="nome" SIZE=%d>""" %len(lista)
	for line in lista:
		print """<OPTION VALUE="%s">%s""" %(line,line)  
	print """</SELECT>"""
        espaco()

#	print """<input type="checkbox" name="ecran_CB" />"""
#        print """Apresentar no monitor <br/>"""
#        print """<input type="checkbox" name="email_CB" />"""
#        print """Enviar email para <input type="text" name="email" />"""
#        print "<br/>"
#        print """<input type="checkbox" name="sms_CB" />"""
#        print """Enviar SMS para <input type="text" name="sms" />"""

	print """<table >"""
	print """<tr>"""
	print """<td><input type="checkbox" name="ecran_CB" /><td/>"""
	print """<td>Apresentar no monitor<td/>"""
	print """<tr/>"""
	print """<tr>"""
        print """<td><input type="checkbox" name="email_CB" /><td/>"""
        print """<td>Enviar email para <td/>"""
	print """<td><input type="text" name="email" value="inserir email"/><td/>"""
	print """<tr/>"""
	print """<tr>"""
        print """<td><input type="checkbox" name="sms_CB" /><td/>"""
        print """<td>Enviar SMS para<td/>"""
	print """<td><input type="text" name="sms" value="inserir telemóvel"/><td/>"""
	print """<tr/>"""
	print """<table/>"""
        espaco()
	print """<INPUT TYPE=SUBMIT value="Submeter">"""
	print "</FORM>"
footer()

