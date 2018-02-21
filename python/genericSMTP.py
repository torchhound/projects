import smtplib

def sendSMTP(sender, receiver, subject, message, server, port, password):
    msg = 'Subject: %s\n\n%s' % (subject, message)
    try:
        smtpObject = smtplib.SMTP('%s, %d' % (server, port))
        smtpObject.ehlo()
        #smtpObject.starttls()
        #smtpObject.ehlo()
        smtpObject.login(sender, password)
        smtpObject.sendmail(sender, receiver, mmsg) #msg.as_string()?
        smtpObject.quit()
    except SMTPException:
        return False