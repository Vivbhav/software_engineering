import mysql.connector
import datetime

from dateutil import parser

cnx = mysql.connector.connect(user='root', password='vivbhav97', host='127.0.0.1', database='project')
cursor = cnx.cursor()

name = raw_input("Enter name of event")

start_time = raw_input("Enter start time of event\n")
dt = parser.parse(start_time)

end_time = raw_input("Enter end time of event\n")
dt_2 = parser.parse(end_time)

cursor.execute(("insert into events values ('{}', '{}', '{}');".format(name, dt, dt_2)))
print (dt)
print (dt_2)
