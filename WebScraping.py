import requests
from bs4 import BeautifulSoup as bs
user=input("Input GitHub User:")
url='https://github.com/'+user
r=requests.get(url)
soup = bs(r.content)
image=soup.find('img',{'alt':'Avatar'})['src']
print(image)
