import smtplib

#SMTP - Simple Mail Transfer Protocol
#Para criar o servidor e enviar o e-mail

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#MIME - Norma de envio de mensagem pela internet

# 01 - Start no servidor SMTP
#host = 'smtp.gmail.com'
#port = '587'
#login = "faturamento.sesgo@gmail.com"
#senha = "gapigapi"

server = smtplib.SMTP('smtp-relay.gmail.com', 587)
#server.ehlo()
server.starttls()

#server.login(login,senha)

#server = smtplib.SMTP_SSL('smtp.gmail.com')
#server.login(login, senha)
#server.sendmail(
#    "faturamento.sesgo@gmail.com",
#    "cpi.sesgo@gmail.com",
#    "mensagem de e-mail de teste"
#)
#server.quit()


# 02 - Construir o email timo MIME

# 03 - Enviar o email tipo MIME no servidor SMTP