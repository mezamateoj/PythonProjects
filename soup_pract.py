import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html').text

soup = BeautifulSoup(data, 'html.parser')

tables = soup.find_all('table')

cacao = pd.DataFrame(columns=['Company', 'Origin', 'REF', 'Review_date', 'Cocoa %', 'Company loc', 'Rating', 'Bean type', 'Bean origin'])

for row in tables[1].find_all('tr'):
    col = row.find_all('td')
    com = col[0].text
    ori = col[1].text
    ref = col[2].text
    rev = col[3].text
    cocoa = col[4].text
    comp = col[5].text
    rating = col[6].text
    b_type = col[7].text
    b_origin = col[8].text
    
    cacao = cacao.append({'Company': com, 'Origin': ori, 'REF': ref,
                           'Review_date': rev, 'Cocoa %': cocoa, 'Company loc': comp,
                           'Rating': rating, 'Bean type': b_type, 'Bean origin': b_origin}, ignore_index=True)

#print(cacao['Rating'].head())
# if a only wnat ratings column 
ratings = []
for row in soup.find_all(attrs={'class': 'Rating'})[1:]:
  ratings.append(float(row.text))

#print(ratings[0:5])

# get company names 
company_tags = soup.select('.Company')
company_name = []
for row in company_tags[1:]:
  company_name.append(row.text)

#print(company_name[0:5])

percent_tags = soup.select('.CocoaPercent')
percent = []
for row in percent_tags[1:]:
  percent.append((row.text).strip('%'))

dic = {'Company': company_name, 'Rating': ratings, 'CocoaPercent': percent}
df = pd.DataFrame.from_dict(dic)
#print(df.head())


plt.scatter(df.CocoaPercent, df.Rating)
plt.tight_layout()
plt.show();
# the mean for all the companies ratings
mean_ratings = df.groupby('Company').Rating.mean()
#print(mean_ratings)

# companies with best ratings
best_companies = mean_ratings.nlargest(10)
#print(best_companies)