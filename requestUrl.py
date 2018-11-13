from bs4 import BeautifulSoup
import requests


gitHub = requests.get('https://github.com/wangxd100')
# return http status code 200
# print(gitHub)

content = gitHub.content
print(content)

soup = BeautifulSoup(content, "html.parser")
allA = soup.findAll("a")

for link in allA:
    print(link)
    print(link.string)

