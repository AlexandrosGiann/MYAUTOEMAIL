from keyword_google_search import search
from email_checker import exists_in_database
from send_emails import send_email
from get_emails_from_websites import GEFW

lst = []

USERNAME = ""
PASSWORD = ""
subject = ""
text = """
"""

for keyword in open("keywords.txt", 'r').readlines():
    keyword = keyword.replace('\n', '')
    search(keyword)
    GEFW()
    print("===============================================================")
    for email in open("result_emails.txt", 'r').readlines():
        email = email.replace('\n', '')
        if exists_in_database(email) and email not in lst:
            lst.append(email)
try:
    send_email(USERNAME, PASSWORD, lst, subject, text)
except:
    print("EMAIL ERROR")
lst1 = [email.replace('\n', '') for email in open("saved_emails.txt", 'r').readlines()]
for email in lst:
    if email not in lst1:
        lst1.append(email)
file = open('saved_emails.txt', 'w')
file.writelines(lst1)
file.close()
input("Press enter to exit...")