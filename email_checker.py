from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def exists_in_database(gmail):
    browser.get("https://accounts.google.com")
    # browser.execute_script('return document.documentElement.innerHTML;')
    email_input = browser.find_element("name", "identifier")
    email_input.clear()
    email_input.send_keys(f"{gmail}\n")
    time.sleep(2)
    code = browser.execute_script('return document.documentElement.innerHTML;')
    return not ("Δεν ήταν δυνατή η εύρεση του Λογαριασμού σας Google." in code or "Couldn't find your Google Account" in code)

if __name__ == "__main__":
    gmail = input("Enter an email:")
    print(exists_in_database(gmail))
