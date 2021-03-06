import requests
import time
from bs4 import BeautifulSoup
with open('6级号.txt', 'a+', encoding='utf-8') as f:
    for i in range(1, 13908237):
        url="https://api.bilibili.com/x/space/acc/info?mid="+str(i)+"&jsonp=jsonp"
        html = requests.get(url).text
        st = str(html)
        pos = st.find('level')
        tot = 0
        if st[pos+7] == '6':
            name = '\n'
            tot += 1
            pos = st.find('name')
            j = pos+7
            while 1:
                if st[j+1] == ',':
                    break
                name += st[j]
                j += 1
            f.write(name)
    f.write(str(tot))
