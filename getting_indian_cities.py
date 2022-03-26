import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable

url = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"

page = requests.get(url)
html_content = page.content
soup = BeautifulSoup(html_content, "html.parser")
table_soup = soup.find_all("table")
header_tag = soup.find_all("th")
head = [header.text.strip() for header in header_tag]
#print(head)
row = []
table = soup.find("table")
data_rows = table.find_all("tr")
for rows in data_rows:
    value = rows.find_all("td")
    value2 = [dp.text.strip() for dp in value]
    #print(value2)
    if len(value2) == 0:
        continue

    row.append(value2)
x = PrettyTable()
x.field_names = ['Rank','City','Population(2011)',
                'Population(2001)','State or union territory']
x.add_rows(row)
print(x)
#print(row)

data = pd.DataFrame(row)
data.columns = ['Rank','City','Popukation(2011)',
                'Population(2001)','State or union territory']
data.to_csv("indian_population.csv", index=0)
