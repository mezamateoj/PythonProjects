import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
prefix = "https://content.codecademy.com/courses/beautifulsoup/"

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
turtle_links = soup.find_all('a')

links = []
for i in turtle_links:
    links.append(prefix + i['href'])

#print(links)
#print(soup.find_all(re.compile("[ou]l")))

#Define turtle_data:
turtle_data = {}
#follow each link:
for link in links:
  page = requests.get(link)
  turtle = BeautifulSoup(page.content, "html.parser")
  # turtle_name = turtle.select('.name')[0] # currently dict has the p tags
  # get rid of p tags 
  turtle_name = turtle.select('.name')[0].get_text()
  
  turtle_data[turtle_name] = turtle.find('ul').get_text('|').split('|')
  
#print(turtle_data)
df = pd.DataFrame(turtle_data)
print(df.head())
