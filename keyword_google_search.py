from googlesearch import search

keyword = input("Enter a keyword:")

for i in range(10):
    print(f'try:{i+1}')
    search_results = search(keyword)
    lst = []
    try:
        while True:
            url = next(search_results)
            print(url)
            lst.append(url + '\n')
    except:
        pass
file = open('urls.txt', 'w')
file.writelines(lst)
file.close()
