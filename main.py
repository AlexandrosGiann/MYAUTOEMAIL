from keyword_google_search import google_search
from email_checker import exists_in_database
from get_emails_from_websites import GEFW

lst = []

for keyword in open("keywords.txt", 'r').readlines():
    keyword = keyword.replace('\n', '')
    google_search(keyword)
    GEFW()
    print("===============================================================")
    for email in open("result_emails.txt", 'r').readlines():
        email = email.replace('\n', '')
        if exists_in_database(email) and email not in lst:
            lst.append(email)
 
lst1 = [email.replace('\n', '') for email in open("saved_emails.txt", 'r').readlines()]
for email in lst:
    if email not in lst1:
        lst1.append(email)
file = open('saved_emails.txt', 'w')
file.writelines(lst1)
file.close()
input("Press enter to exit...")
