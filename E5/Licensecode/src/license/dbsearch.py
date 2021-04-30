import sqlite3
from ult.config import *
from ult.ServerAct import initDB

def deleteLicense(Lno):
    conn = sqlite3.connect(databaseName)
    curs = conn.cursor()
    try:
        sql = "delete from client where lno='" + Lno + "'"
        curs.execute(sql)
        conn.commit()
        sql = "delete from license where lno='" + Lno + "'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        conn.close()
        return False

def deleteClient(Tno, Lno):
    conn = sqlite3.connect(databaseName)
    curs = conn.cursor()
    try:
        sql = "delete from client where lno='" + Lno + "' and tno='"+Tno+"'"
        curs.execute(sql)
        conn.commit()
        sql = "delete from license where lno='" + Lno + " and tno='"+Tno+"'"
        curs.execute(sql)
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        conn.close()
        return False

def searchAll(table):
    conn = sqlite3.connect(databaseName)
    curs = conn.cursor()
    sql = "select * from " + table
    try:
        curs.execute(sql)
    except sqlite3.OperationalError:
        initDB()
        curs.execute(sql)
    res = curs.fetchall()

    colsql = "PRAGMA table_info([" + table + "])"
    curs.execute(colsql)
    collist = curs.fetchall()

    response = '<table class="table table-striped"><tr>'
    for colinfo in collist:
        response += '<th>' + colinfo[1] + '</th>'
    response += '<th>Option</th></tr>'
    for var in res:
        response += '<tr>'
        for col in var:
            response += '<td>' + str(col) + '</td>'
        if table == 'license':
            response += "<td><a href='/deleteLicense/?Lno="
            response += var[0]
            response += "'>delete</a></td>"
        else:
            response +="<td><a href='/deleteClient/?Tno="
            response += var[0]
            response +="&Lno="
            response += var[2]
            response += "'>delete</a></td>"
        response += '</tr>'
    return response + "</table>"