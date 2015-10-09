#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="192.168.1.10",
                     user="translink",
                      passwd="translink123",
                      db="translink")

cur = db.cursor()

cur.execute("SHOW TABLES")

for row in cur.fetchall():
    print str(row)
