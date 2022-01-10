<<<<<<< HEAD
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

# 02 - Construir o email timo MIME/HTML
assunto = "Teste com arquivo do Juarez Barbosa"
corpo = """
<p>Teste com arquivos grande para envio de Prévia da Síntese de Produção Ambulatorial<br>
Verificar ajustes e corrigir até 15/01/2022<br><br>
Att.<br>Alexandre Damaso</p>
"""

# Seletores de envio
dtn_ALEXANDRE = 1
dtn_EDNA = 1
dtn_ZECARLOS = 1

# lista de e-mails
email_ZECARLOS = "josecarlosgo@gmail.com"
email_EDNA = "edna.prado@goias.gov.br"
email_ALEXANDRE = "alexandredamasocosta@gmail.com"

#Alexandre Damaso
if dtn_ALEXANDRE == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_ALEXANDRE
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\SFinal\R507-JB.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-JB.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

#EDNA
if dtn_EDNA == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_EDNA
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\SFinal\R507-JB.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-JB.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

    #ZE CARLOS
if dtn_ZECARLOS == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_ZECARLOS
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\SFinal\R507-JB.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-JB.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

server.quit()
=======
# teste de amail
>>>>>>> 09c566eb641e2d2bbac82d25adeffc33c7b1c413
