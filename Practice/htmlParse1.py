import bs4


soup = bs4.BeautifulSoup(open(r'c:\PythonProjects\ball_schedule.html'), 'html.parser')

elems = soup.findAll(id='schedRow4152048')

for i in elems:
    print(i)