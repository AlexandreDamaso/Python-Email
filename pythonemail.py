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
# CONTROLE DE ENVIO DE EMAIL PARTINDO DE ZERO
dtn_PRP = 0
dtn_HCAMP = 0
dtn_PEG = 0
dtn_PEQ = 0
dtn_JB = 0
dtn_HUGO = 0
dtn_LACEN = 0
dtn_HGG = 0
dtn_HEMOGO = 0
dtn_HEMNSL = 0
dtn_HMI = 0
dtn_CAPSI = 0
dtn_COEG = 0
dtn_HEL = 0
dtn_HEJA = 0
dtn_SLMB = 0
dtn_HEELJ = 0
dtn_HDT = 0
dtn_HEF = 0
dtn_HEJ = 0
dtn_HSC = 0
dtn_HEI = 0
dtn_HDS = 0
dtn_CREMIC = 0
dtn_CRER = 0
dtn_IOAL = 0
dtn_HEANA = 0
dtn_HETRIN = 0
dtn_SUVISACEREST = 0
dtn_HERSO = 0
dtn_CLIMER = 0
dtn_HPET = 0
dtn_HUGOL = 0
dtn_CREDEQ = 0
dtn_TFD = 0
dtn_CEAPSOL = 0

"""
# CONTROLE DE ENVIO DE EMAIL PARTINDO DE UM
dtn_PRP = 1
dtn_HCAMP = 1
dtn_PEG = 1
dtn_PEQ = 1
dtn_JB = 1
dtn_HUGO = 1
dtn_LACEN = 1
dtn_HGG = 1
dtn_HEMOGO = 1
dtn_HEMNSL = 1
dtn_HMI = 1
dtn_CAPSI = 1
dtn_COEG = 1
dtn_HEL = 1
dtn_HEJA = 1
dtn_SLMB = 1
dtn_HEELJ = 1
dtn_HDT = 1
dtn_HEF = 1
dtn_HEJ = 1
dtn_HSC = 1
dtn_HEI = 1
dtn_HDS = 1
dtn_CREMIC = 1
dtn_CRER = 1
dtn_IOAL = 1
dtn_HEANA = 1
dtn_HETRIN = 1
dtn_SUVISACEREST = 1
dtn_HERSO = 1
dtn_CLIMER = 1
dtn_HPET = 1
dtn_HUGOL = 1
dtn_CREDEQ = 1
dtn_TFD = 1
dtn_CEAPSOL = 1
"""

# E-MAIL
email_PRP = "faturamento@policlinicaposse.org.br"
email_HCAMP = "faturamentohcamp@gmail.com"
email_PEG = "faturamento@policlinicagoianesia.org.br"
email_PEQ = "faturamento@policlinicaquirinopolis.org.br"
email_JB = "cmacjuarezbarbosa@gmail.com"
email_HUGO = "patriciachaul@ints.org.br"
email_LACEN = "wagno.souza@goias.gov.br"
email_HGG = "cleverson.chaves@idtech.org.br"
email_HEMOGO = "hemocentro.faturamento@idtech.org.br"
email_HEMNSL = "faturamento.mnsl@igh.org.br"
email_HMI = "faturamento.hmi@igh.org.br"
email_CAPSI = "capsiestadual@gmail.com"
email_COEG = "faturamento.68@gmail.com"
email_HEL = "faturamento@hospital-luziania.org.br"
email_HEJA = "faturamento@hejago.org.br"
email_SLMB = "faturamento@hospital-drgeraldolando.org.br"
email_HEELJ = "faturamento.heelj@gmail.com"
email_HDT = "faturamento.hdt@isgsaude.org"
email_HEF = "coordenacao.faturamento@hospital-formosa.org.br"
email_HEJ = "sergio.jr@safatle.com.br"
email_HSC = "braulia.malaspina@cottolengo.org.br"
email_HEI = "faturamento.hri@ints.org.br"
email_HDS = "faturamento@hds.org.br"
email_CREMIC = "faturamentocremic@gmail.com"
email_CRER = "faturamento@crer.org.br"
email_IOAL = "wlspab@gmail.com"
email_HEANA = "supervisaofaturamento@hospitaldeurgencias.com.br"
email_HETRIN = "faturamento@hospital-hutrin.org.br"
email_SUVISACEREST = "planejamento.suvisa@gmail.com"
email_HERSO = "faturamento@herso.org.br"
email_CLIMER = "climernefrologia@gmail.com"
email_HPET = "faturamento.hpet@alsf.org.br"
email_HUGOL = "faturamentohugol@gmail.com"
email_CREDEQ = "faturamento@credeq-go.org.br"
email_TFD = "tfdgoias@gmail.com"
email_CEAPSOL = "faturamento.cs@isgsaude.org"

# PRP - POSSE
if dtn_PRP == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_PRP
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-PRP.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-PRP.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HCAMP
if dtn_HCAMP == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HCAMP
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HCAMP.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HCAMP.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# PEG
if dtn_PEG == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_PEG
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-PEG.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-PEG.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# PEQ
if dtn_PEQ == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_PEQ
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-PEQ.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-PEQ.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# JB
if dtn_JB == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_JB
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-JB.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-JB.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HUGO
if dtn_HUGO == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HUGO
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HUGO.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HUGO.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# LACEN
if dtn_LACEN == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_LACEN
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-LACEN.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-LACEN.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HGG
if dtn_HGG == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HGG
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HGG.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HGG.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEMOGO
if dtn_HEMOGO == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEMOGO
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEMOGO.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEMOGO.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEMNSL
if dtn_HEMNSL == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEMNSL
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEMNSL.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEMNSL.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HMI
if dtn_HMI == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HMI
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HMI.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HMI.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CAPSI
if dtn_CAPSI == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CAPSI
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CAPSI.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CAPSI.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# COEG
if dtn_COEG == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_COEG
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-COEG.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-COEG.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEL
if dtn_HEL == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEL
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEL.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEL.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEJA
if dtn_HEJA == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEJA
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEJA.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEJA.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# SLMB
if dtn_SLMB == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_SLMB
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-SLMB.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-SLMB.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEELJ
if dtn_HEELJ == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEELJ
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEELJ.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEELJ.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HDT
if dtn_HDT == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HDT
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HDT.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HDT.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEF
if dtn_HEF == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEF
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEF.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEF.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEJ
if dtn_HEJ == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEJ
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEJ.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEJ.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HSC
if dtn_HSC == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HSC
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HSC.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HSC.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEI
if dtn_HEI == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEI
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEI.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEI.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HDS
if dtn_HDS == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HDS
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HDS.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HDS.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CREMIC
if dtn_CREMIC == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CREMIC
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CREMIC.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CREMIC.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CRER
if dtn_CRER == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CRER
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CRER.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CRER.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# IOAL
if dtn_IOAL == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_IOAL
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-IOAL.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-IOAL.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HEANA
if dtn_HEANA == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HEANA
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HEANA.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HEANA.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HETRIN
if dtn_HETRIN == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HETRIN
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HETRIN.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HETRIN.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# SUVISACEREST
if dtn_SUVISACEREST == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_SUVISACEREST
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-SUVISACEREST.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-SUVISACEREST.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HERSO
if dtn_HERSO == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HERSO
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HERSO.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HERSO.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CLIMER
if dtn_CLIMER == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CLIMER
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CLIMER.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CLIMER.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string()) 

# HPET
if dtn_HPET == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HPET
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HPET.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HPET.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# HUGOL
if dtn_HUGOL == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_HUGOL
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-HUGOL.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-HUGOL.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CREDEQ
if dtn_CREDEQ == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CREDEQ
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CREDEQ.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CREDEQ.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# TFD
if dtn_TFD == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_TFD
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-TFD.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-TFD.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

# CEAPSOL
if dtn_CEAPSOL == 1:
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email_CEAPSOL
    email_msg['Subject'] = assunto
    email_msg.attach(MIMEText(corpo,'html'))
    anexo = "C:\sfinal\R507-CEAPSOL.zip"
    attchment = open(anexo,'rb')
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename=R507-CEAPSOL.zip')
    attchment.close()
    email_msg.attach(att)
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

server.quit()