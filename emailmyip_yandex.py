import smtplib

def emailmyip(newip,lastip):
    email = "???@yandex.ru"
    password = "???"
    dest_email = "???@???.???"
    subject = "new ip"
    email_text = "new ip: {}\nlast ip:{}".format(newip,lastip)

    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                       dest_email,
                                                       subject,
                                                       email_text)


    server = smtplib.SMTP_SSL()
    server.connect('smtp.yandex.ru')
    server.login(email, password)
    server.sendmail(email,dest_email,message)
    server.quit()
