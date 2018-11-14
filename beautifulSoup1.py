from bs4 import BeautifulSoup
import math
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
    print(item)
    if "H1" in item.string:
        print(item.string)

print('-----------------------')

#############  Testing FOR loop syntax ###########
for x in range(0, 3):
    print("We're on time %d" % (x))

for x in "banana":
  print(x)
print('-----------------------')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print('-----------------------')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)

print('-----------------------')