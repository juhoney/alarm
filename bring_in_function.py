from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from add_function import *

app = Flask(__name__)

#delete_work()
#conn = sqlite3.connect("test.db")

try:
    cur.execute("CREATE TABLE homework(no INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, subject TEXT, term TEXT, time TEXT, ranges TEXT, place TEXT)")
    conn.commit()
except:
    pass
#번호, 이름, 과목, 기간, 시간, 범위, 장소
#input_db('과학 숙제', '과학', '2020-09-20', '60min', '1p ~ 200p', '교무실')

flag = 0
@app.route('/')
def bring():
    print('flag', flag)
    # if request.method == 'POST':
        #conn = sqlite3.connect("test.db")
        #cur = conn.cursor()
        #cur.execute('select * from homework')
        #rows = cur.fetchall()
        #for row in rows:
            #print(row)
    con = sqlite3.connect('test.db')
    query = "select * from turing"
    cur = con.cursor()
    cur.execute(query)

    works = []
    rows = cur.fetchall()
    for row in rows:
        works.append(list(row))
    print(works)

    return render_template("homework_notice.html", rows=works, flag=flag)

@app.route('/close', methods=['POST'])
def close_board():
    print('c')
    global flag
    flag = 0
    return redirect(url_for('bring'))


@app.route('/bring', methods=['POST'])
def bring_board():
    print('b')
    global flag
    flag = 1
    return redirect(url_for("bring"))
'''
def bring_in():
    for line in lines:

        temp_name = line.split(',')
        #if temp_name[4] == "학원":
            #temp_name[4] = "복도"

        v = temp_name[0]

        for i in range(1, len(temp_name)):
            v = v + ',' + temp_name[i]

        fw.writelines(v)
'''

if __name__ == '__main__':
    app.run()