from bs4 import BeautifulSoup
import requests


gitHub = requests.get('https://github.com/wangxd100')
# return http status code 200
# print(gitHub)

content = gitHub.content
# print(content)

soup = BeautifulSoup(content, "html.parser")
allA = soup.findAll("a")
title = soup.findAll("title")
# print(title)

# for link in allA:
    # print(link)
    # print(link.string)


soup2 = BeautifulSoup(content, "html.parser")
attrs = soup2.body.div.attrs
print(attrs)
