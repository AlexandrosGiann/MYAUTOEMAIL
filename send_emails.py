import yagmail
def send_email(username, password, emails, subject, test)
    yag = yagmail.SMTP(username, password)
    yag.send(emails,subject,test)
