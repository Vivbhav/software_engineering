import mysql.connector
import datetime

from dateutil import parser

#conn = mysql.connector.connect(database="events", user="root", host="127.0.0.1", password="vivbhav97")
#cursor = conn.cursor(buffered=True)

start_time = raw_input("Enter start time of event\n")
dt = parser.parse(start_time)

end_time = raw_input("Enter end time of event\n")
dt_2 = parser.parse(end_time)

print (dt)
print (dt_2)

