import requests

#get a webpage

r = requests.get('https://api.github.com/events')

#make HTTP POST request

p = requests.post('https://httpbin.org/post', data={'morning': 'coffee'})


print(r)
print(p)




