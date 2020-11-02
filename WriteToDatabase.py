import sqlite3

''' წერს დატაბაზაში values() ებს სკრაპ დიქტიდან  და არ ვწვდები მათ სახელით'''
'''მომავალში ამის დროზე აუტომატიზაცია იქნება საჭირო'''
from NewsScrap import scrapping

scrp = scrapping()

val = (tuple(i.values()) for i in scrp)

try:
    conn = sqlite3.connect('news_db.sqlite')
    cursor = conn.cursor()
    cursor.executemany(
        'INSERT OR IGNORE INTO news_piece (title, date_time, content, photo_url_main) VALUES(?, ?, ?, ?)', val)
except sqlite3.Error as error:
    print("Failed to insert Python variable into sqlite table", error)

conn.commit()
conn.close()
