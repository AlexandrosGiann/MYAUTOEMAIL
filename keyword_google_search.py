from googlesearch import search

def google_search(keyword):
    lst = []
    search_results = search(keyword)
    try:
        while True:
            url = next(search_results)
            lst.append(url + '\n')
    except:
        pass
    file = open('urls.txt', 'w')
    file.writelines(lst)
    file.close()
if __name__ == '__main__':
    google_search('yugioh')
    print(open('urls.txt', 'r').read())
