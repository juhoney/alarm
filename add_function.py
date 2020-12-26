from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("test.db")
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE turing(no INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, subject TEXT, term TEXT, time TEXT, ranges TEXT, place TEXT)")
    conn.commit()
    conn.close()
except:
    pass

"""
@app.route('/')
def main_screen():
    return render_template('homework_notice.html')

@app.route("/kkk", methods=["POST"])
def add():

    if request.method == 'POST':
        temp1 = request.form['number']
        temp2 = request.form['name']
        temp3 = request.form['subject']
        temp4 = request.form['term']
        temp5 = request.form['time']
        temp6 = request.form['ranges']
        temp7 = request.form['place']
    cur.execute("INSERT INTO turing(name, subject, term, time, ranges, place) VALUES(?, ?, ?, ?, ?, ?, ?)")

    conn.commit()
    conn.close()
    return render_template('homework_notice.html')
"""

def input_db(name, subject, term, time, ranges, place):
    conn = sqlite3.connect('test.db')

    rel = "INSERT INTO turing(name, subject, term, time, ranges, place) VALUES(?, ?, ?, ?, ?, ?)"
    conn.execute(rel, (name, subject, term, time, ranges, place))

    conn.commit()
    conn.close()



def delete_work(num):
    conn = sqlite3.connect("test.db")
    delQuery = "DELETE FORM work WHERE no=?"
    conn.execute(delQuery, (num, ))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run()