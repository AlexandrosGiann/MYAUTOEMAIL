import yagmail
def send_email(username, password, emails, subject, text):
    yag = yagmail.SMTP(username, password)
    yag.send(emails,subject,text)
