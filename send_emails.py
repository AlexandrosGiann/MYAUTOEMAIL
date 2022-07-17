import yagmail

USERNAME = ""
PASSWORD = ""
subject = ""
text = """
"""

def send_email(username, password, emails, subject, text):
    yag = yagmail.SMTP(username, password)
    yag.send(emails,subject,text)
