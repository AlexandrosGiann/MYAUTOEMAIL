import yagmail

USERNAME = ""
PASSWORD = ""
subject = ""
text = """
"""

def send_email(username, password, emails, subject, text):
    yag = yagmail.SMTP(username, password)
    yag.send(emails,subject,text)


if __name__ == '__main__':
    emails = [email for email in open('saved_emails.txt', 'r').readlines()]
    send_email(USERNAME, PASSWORD, emails, subject, text)
