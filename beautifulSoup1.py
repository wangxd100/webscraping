from bs4 import BeautifulSoup
myHtml = '''<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<h1>2nd H1 tage</h1>
<p>My first paragraph.</p>

</body>
</html>
'''



soup = BeautifulSoup(myHtml, 'html.parser')
myH1 = soup.findAll("h1")

for item in myH1:
    if "H1" in item.string:
        print(item.string)




