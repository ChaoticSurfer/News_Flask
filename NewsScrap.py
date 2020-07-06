from datetime import datetime
import requests
from bs4 import BeautifulSoup
# from time import sleep
# from random  import randrange
'''მოთხოვნის მიხედვით დავწერე ძილი მაგრამ არ არის საჭირო ამიტომ დაკომენტარებულია'''


'''
ambebi.ge დან მოაქ ყველა a თეგი დამანდედან არჩევს სტატიებს რომლებსაც შემდგომ ამუშავებს
დატაბაზისთვის ვქმნი datetime  ობიექტებტებს
'''

def scrapping():
    url = "https://www.ambebi.ge/"
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find_all('a')
    article_urls = []
    result = []

    for tag in tags:
        a = str(tag.get('href'))
        if a.startswith('/article'):
            article_urls.append('https://www.ambebi.ge' + a)

    for url in article_urls:
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        article_block = soup.find_all('div', {'class': 'article_block'})

        for i in article_block:
            title = str(i.find('h1').text.replace('\n', ""))
            time = i.find('div').text.replace('\n', "").strip()
                                                        # datetime.strptime('10:34 / 02-07-2020','%H:%M / %d-%m-%Y')
            time = datetime.strptime(time, '%H:%M / %d-%m-%Y')  # format
            content = i.find('div', {'class': 'article_content'}).text.strip('\n')
            photo_url_main = "https:" + i.select_one('img.picture').get('data-src')
            # sleep(randrange(10,20))

        result.append({'title': title, 'time': time, 'content': content, 'photo': photo_url_main})
    return result
