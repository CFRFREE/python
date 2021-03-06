import requests
import time
from bs4 import BeautifulSoup

base_url = "https://www.bilibili.com/v/popular/rank/all"

html = requests.get(base_url).text

soup = BeautifulSoup(html, 'html.parser')

comments = []
rank = 0

liTags = soup.find_all('li', attrs={'class': 'rank-item'})
for li in liTags:
    comment = {}
    comment['title'] = li.find('a', class_='title').string
    comment['link'] = li.find('a', class_='title').get('href')
    st = str(li.find('span', class_='data-box up-name'))
    comment['up'] = st[77:-21]
    comments.append(comment)

date=time.strftime("%Y-%m-%d", time.localtime())
txt_name=date+'B站热榜.txt'
with open(txt_name, 'a+', encoding='utf-8') as f:
    f.seek(0)
    f.truncate()
    f.write(time.strftime("%Y-%m-%d", time.localtime()))
    f.write('\n')
    for comment in comments:
        rank += 1
        f.write('排名：{} \t标题：{} \t\t 链接：{} \t\t up主： {}'.format(
            rank, comment['title'], comment['link'], comment['up']))
    print('DONE！')
