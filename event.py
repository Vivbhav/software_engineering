import MySQLdb
import datetime
from dateutil import parser

cnx = MySQLdb.connect("localhost","root","vivbhav97","events" )
#cnx.query('SET GLOBAL connect_timeout=6000')
cursor = cnx.cursor()

def create_event(): 
    name = raw_input("Enter name of event")

    start_time = raw_input("Enter start time of event\n")
    dt = parser.parse(start_time)

    end_time = raw_input("Enter end time of event\n")
    dt_2 = parser.parse(end_time)

    cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(name, dt, dt_2)))
    cursor.execute(("commit;"))
    #print cursor.execute(("insert into events_list(event_name,start_time,end_time) values('c', 'b', 'a');"))

def delete_event(name):
    cursor.execute(("select event_id from events_list where event_name='{}';".format(name)))
    a = cursor.fetchone()
        
    
create_event()


cursor.close();
