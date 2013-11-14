GENERIC_DOMAINS = "aero", "asia", "biz", "cat", "com", "coop", \
        "edu", "gov", "info", "int", "jobs", "mil", "mobi", "museum", \
        "name", "net", "org", "pro", "tel", "travel"


#credit to http://commandline.org.uk/python/email-syntax-check/
def invalidemail(emailaddress, domains = GENERIC_DOMAINS):
        """Checks for a syntactically invalid email address."""

        # Email address must be 7 characters in total.
        if len(emailaddress) < 7:
            return True # Address too short.

        # Split up email address into parts.
        try:
            localpart, domainname = emailaddress.rsplit('@', 1)
            host, toplevel = domainname.rsplit('.', 1)
        except ValueError:
            return True # Address does not have enough parts.

        # Check for Country code or Generic Domain.
        if len(toplevel) != 2 and toplevel not in domains:
            return True # Not a domain name.

        for i in '-_.%+.':
            localpart = localpart.replace(i, "")
        for i in '-_.':
            host = host.replace(i, "")

        if localpart.isalnum() and host.isalnum():
            return False # Email address is fine.
        else:
            return True # Email address has funny characters.


def invalidphone(phone):
#       print phone
        #check for int type
        if type(phone).__name__ == 'int' or type(phone).__name__ == 'long':
#                print "int"
                if phone > 900000000 and phone < 999999999:
#                        print "nice"
                        return False
                else: 
                        return True
        else:
                if not (len(phone) == 9 or len(phone) == 13):
#                        print "not right size"
                        return True 
                if phone.isdigit():
#                        print "is digits"
                        return False
                if phone[0] == '+' and phone[1:len(phone)].isdigit():
#                        print "+ and digits"
                        return False
#                print "not cool"
                return True 

#function for email
def sendemail(TO, message):
     import smtplib
     SERVER = "localhost"
     FROM = "MUDAR EMAIL"
     #TO = ["user@example.com"] # must be a list
     TO = [TO]
     SUBJECT = "Natal!"
     message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT,message)

     # Send the mail
     server = smtplib.SMTP(SERVER)
     server.sendmail(FROM, TO, message)
     server.quit()

#fucntion for sms
def sendsms(tlmdestino, texto):
                username="MUDAR USER"
                password="MUDAR PASS"
                tlmorigem="MUDAR TELEMOVEL"
#                espaco()
                gettext="/enviar_sms_get.php?username=" + username + "&password=" + \
password + "&origem=" + tlmorigem + "&destino=" + tlmdestino + "&mensagem=" + texto
                gettext = gettext.replace(" ","+")
#                print gettext
#                espaco()
                import httplib
                conn = httplib.HTTPConnection("www.lusosms.com")
                conn.request("GET", gettext)
                r1 = conn.getresponse()
#                print r1.status, r1.reason
                espaco()
                data1 = r1.read()
                print data1
                conn.close()

#function for space 
def espaco():
#	print "<br/>"
	print "<br/>"
	print "<br/>"

#function for html header
def header():
	print "Content-Type: text/html\n"
	print """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
	<HTML>
	   <HEAD>
		<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-15">
	      <TITLE>Sorteio de Natal</TITLE>
	</HEAD>
	<BODY>
	<center>"""

#function for html footer
def footer():
	print """</center></BODY></HTML>"""

