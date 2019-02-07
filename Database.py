import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from  matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('attempt1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS theAttempt(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO theAttempt VALUES(1437817, '2016-01-01', 'Python', 123)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO theAttempt (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    #c.execute("SELECT keyword, unix value, datestamp FROM theAttempt WHERE value=3 AND keyword='Python'")
    c.execute("SELECT * FROM theAttempt WHERE value=3 AND keyword='Python'")
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        #print(row[0])
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM theAttempt')
    dates = []
    values = []
    for row in c.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt. plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM theAttempt')
    [print(row) for row in c.fetchall()]

    # c.execute('UPDATE theAttempt SET value = 99 WHERE value= 2')
    # conn.commit()
    #
    # c.execute('SELECT * FROM theAttempt')
    # [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM theAttempt WHERE value = 99')
    conn.commit()
    print(50*'#')

    c.execute('SELECT * FROM theAttempt')
    [print(row) for row in c.fetchall()]


# create_table()
# #data_entry()
# read_from_db()
# graph_data()
del_and_update()


# for i in range(10):
#     dynamic_data_entry()
#     # Next line for updating time
#     time.sleep(1)


c.close()
conn.close()


