from googlesearch import search

def search(keyword):
    lst = []
    try:
        while True:
            url = next(search_results)
            lst.append(url + '\n')
    except:
        pass
    file = open('urls.txt', 'w')
    file.writelines(lst)
    file.close()
