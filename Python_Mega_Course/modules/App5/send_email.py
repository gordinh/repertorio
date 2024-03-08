import smtplib, ssl

def send_email(message):
  host = "smtp.gmail.com"
  port = 465

  username = "lucas.ecomp2012@gmail.com"
  password = "wuzo trhs gjgc gjaf"

  receiver = "lucas.morais@admobilize.com"
  context  = ssl.create_default_context()

  with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(user=username, password=password)
    server.sendmail(username, receiver, message)
    print(">>>>>>>>>>>>")