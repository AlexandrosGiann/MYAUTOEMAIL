from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import re
import warnings
warnings.filterwarnings("ignore")

os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_LOCAL'] = '1'
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def GEFW():
    lst = []
    for url in open('urls.txt', 'r').readlines():
        url = url.replace('\n', '')
        browser.get(url)
        code = browser.execute_script('return document.documentElement.innerHTML;')
        match = re.findall(r'[\w\.-]+@[\w\.-]+', code)
        lst.append(list(set([email for email in match if email[-1] != '.' and not email[-1].isnumeric()])))
    print(lst)
    lst1 = []
    for l in lst:
        for l1 in l:
            if l1 not in lst1:
                lst1.append(l1)
    result_emails = open("result_emails.txt", 'w')
    result_emails.writelines(lst1)
    result_emails.close()

