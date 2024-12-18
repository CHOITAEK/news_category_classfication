from bs4 import BeautifulSoup
import requests

import re
import pandas as pd
import datetime


category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']

url = 'https://news.naver.com/section/100'


# resp = requests.get(url)
# print(list(resp))
# soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
#
# title_tags = soup.select('.sa_text_strong')
# print(title_tags[0].text)

# for title_tag in title_tags:
#     print(title_tag.text)

df_titles = pd.DataFrame()

for i in range(6):
    url = 'https://news.naver.com/section/10{}'.format(i)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.sa_text_strong')
    titles = []
    for title_tag in title_tags:
        title = title_tag.text
        titles.append(title)

    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)

print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts())
df_titles.to_csv('./crawling_data/naver_headline_news_{}'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)