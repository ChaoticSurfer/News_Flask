import sqlite3
''' წერს დატაბაზაში values() ებს სკრაპ დიქტიდან  და არ ვწვდები მათ სახელით'''
'''მომავალში ამის დროზე აუტომატიზაცია იქნება საჭირო'''
from NewsScrap import scrapping

scrp = scrapping()

val = (tuple(i.values()) for i in scrp)

conn = sqlite3.connect('news_db.sqlite')
cursor = conn.cursor()

cursor.executemany('INSERT INTO news_piece (title, date_time, content, photo_url_main) VALUES(?, ?, ?, ?)', val)

conn.commit()
conn.close()
