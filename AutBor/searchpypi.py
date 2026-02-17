import requests, sys, webbrowser, bs4

headers = {'user-agent': 'Mozilla/5.0 (Linux; rv:1.0)'}

print('Searching...')  # display text while downloading search results page

res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]), headers=headers)   # join converts cli arguments to string

print(res.text)
# TODO: Retrieve top search results links.

soup = bs4.BeautifulSoup(res.text, 'html.parser')


# TODO: Open a browswer tab for each result

linkElems = soup.select('.package-snippet')
print(linkElems)

numOpen = min(5, len(linkElems)) #open the min of 5 or length of list
print(f'numOpen = {numOpen}')
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
