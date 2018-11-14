from bs4 import BeautifulSoup
import requests


gitHub = requests.get('https://github.com/wangxd100')
# return http status code 200
print("status code:",gitHub.status_code)

content = gitHub.content
# print(content)

soup = BeautifulSoup(content, "html.parser")
allA = soup.findAll("a")
title = soup.findAll("title")

print('------ print title --------')
print(title)
print(soup.title.string)
print(soup.title.text)



print('------ print links --------')
for link in allA:
    if len(link)>0:
        #print(link)
        print(link.string)


soup2 = BeautifulSoup(content, "html.parser")
attrs = soup2.body.div.attrs
print(attrs)
