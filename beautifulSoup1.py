from bs4 import BeautifulSoup
myHtml = '''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
'''



soup = BeautifulSoup(myHtml, 'html.parser')
myH1 = soup.find("h1")
print(myH1)
# print only content
print(myH1.string)



