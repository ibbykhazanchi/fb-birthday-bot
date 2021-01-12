import smtplib

def send_text(from_mail, password, to_number):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_mail, password)
    
    message = 'Happy Birthday! Hope you have a good one'

    #try different mails
    server.sendmail(from_mail, '{}@vtext.com'.format(to_number), message)
    server.sendmail(from_mail, '{}@mms.att.net'.format(to_number), message)
    server.sendmail(from_mail, '{}@pm.sprint.com'.format(to_number), message)

    #mail for tmobile has a different format
    t_message = ("From: %s\r\n" % from_mail + "To: %s\r\n" % '{}@tmomail.net'.format(to_number) + "Subject: %s\r\n" % '' + "\r\n" + message)
    server.sendmail(from_mail, '{}@tmomail.net'.format(to_number), t_message)
    server.quit()



