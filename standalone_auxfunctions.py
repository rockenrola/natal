
import http.client

LUSOSMS_USER="CHANGE USER"
LUSOSMS_PASS="CHANGE PASS"
LUSOSMS_NUMBER="CHANGE NUMBER"

GMAIL_USER="CHANGE USER"
GMAIL_PASS="CHANGE PASS"

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

def send_mail(recipient, message, subject):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    msg = MIMEMultipart()
    msg['From'] = GMAIL_USER
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(GMAIL_USER, GMAIL_PASS)
    mailServer.sendmail(GMAIL_USER, recipient, msg.as_string())
    mailServer.close()
