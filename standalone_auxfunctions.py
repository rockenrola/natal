import smtplib
import http.client

LUSOSMS_USER="CHANGE USER"
LUSOSMS_PASS="CHANGE PASS"
LUSOSMS_NUMBER="CHANGE NUMBER"
EMAIL_FROM="CHANGE EMAIL"
EMAIL_USER="CHANGE EMAIL"
EMAIL_PASS="CHANGE PASS"

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

def sendemail(emaildestino, subject, message):
    smtpserver='smtp.gmail.com'
    smtpport=587
    header  = 'From: %s\n' % EMAIL_FROM
    header += 'To: %s\n' % emaildestino
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver, smtpport)  # use both smtpserver  and -port 
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    problems = server.sendmail(EMAIL_FROM, emaildestino, message)
    server.quit()


