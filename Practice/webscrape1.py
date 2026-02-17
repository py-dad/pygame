import requests, sys, webbrowser, bs4, pyperclip

# headers = {'user-agent': 'Mozilla/5.0 (Linux; rv:1.0)'}

print('Searching...')  # display text while downloading search results page

res = requests.get('https://fllbaseball.com/teams/default.asp?u=FRANKLINLITTLELEAGUE&s=baseball&p=schedule')
print(res.text)


pyperclip.copy(res.text)

soup = bs4.BeautifulSoup(res.text, 'html.parser')


elems = soup.select()

print(elems)
