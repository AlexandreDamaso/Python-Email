import smtplib
#SMTP - Simple Mail Transfer Protocol
#Para criar o servidor e enviar o e-mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#MIME - Norma de envio de mensagem pela internet
from email.mime.base import MIMEBase
from email import encoders

# 01 - Start no servidor SMTP
host = "smtp.gmail.com"
port = "587"
login = "cpi.sesgo@gmail.com"
senha = "Cpi_32014991"

server = smtplib.SMTP(host, port)
server.ehlo()
server.starttls()
server.login(login,senha)

# 02 - Construir o email timo MIME
assunto = "Prévia da Síntese de Produção Ambulatorial - 12/2021"
corpo = """
<p>Prévia da Síntese de Produção Ambulatorial - 12/2021<br>
Verificar ajustes e corrigir até 15/01/2022<br><br>
Att.<br>Alexandre Damaso</p>
"""
dtnAlexandre = 1
dtnCanecas = 1

#Alexandre Damaso
if dtnAlexandre == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = "alexandredamasocosta@gmail.com"
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\SFinal\R507-ALEXANDRE.txt"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-ALEXANDRE.txt')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

#Aliança Canecas
if dtnCanecas == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = "aliancacanecas@gmail.com"
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\SFinal\R507-CANECAS.txt"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CANECAS.txt')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

server.quit()