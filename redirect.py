# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 03:43:49 2018

@author: zhang
"""

import os
from flask import Flask,redirect
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Potato456@zz",  # your password
                     db="vccontacts")        # name of the data base
cur = db.cursor()

"""
sql="update testcase set `Counter` = `Counter` + 1 where `ID` ='4848748';"
cur.execute(sql)
db.commit()
"""

app = Flask(__name__)

@app.route('/')
def hello():
    sql="update testcase set `Counter` = `Counter` + 1 where `ID` ='4848748';"
    cur.execute(sql)
    db.commit()
    return redirect("https://www.cuges.org/", code=302)


@app.route('/page2')
def hi():
    sql="update testcase set `Counter` = `Counter` + 1 where `ID` ='4896465';"
    cur.execute(sql)
    db.commit()
    return redirect("https://www.columbia.edu/", code=302)

@app.route('/page3')
def ho():
    sql="update testcase set `Counter2` = `Counter2` + 1 where `ID` ='48943123';"
    cur.execute(sql)
    db.commit()
    return redirect("https://econ.columbia.edu/", code=302)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='104.244.92.138', port=port)


    
    
    