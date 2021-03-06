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
    print (name)
    cursor.execute(("delete from events_list where event_name='{}';".format(name)))
    cursor.execute(("commit;"))

def modify_event():
    name = raw_input("Enter name of event to modify")

    start_time = raw_input("Enter new start time of event\n")
    dt = parser.parse(start_time)

    end_time = raw_input("Enter new end time of event\n")
    dt_2 = parser.parse(end_time)

    cursor.execute(("delete from events_list where event_name='{}';".format(name)))
    cursor.execute(("commit;"))

    cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(name, dt, dt_2)))
    cursor.execute(("commit;"))
 
def add_task():
    name = raw_input("Enter name of task")   
    duration = raw_input("Enter estimated duration of task\n")
    cursor.execute(("insert into tasks(task_name,duration) values('{}', '{}');".format(name, duration)))
    cursor.execute(("commit;"))

def finish_task():
    name = raw_input("Enter name of task finished")   
    cursor.execute(("delete from tasks where task_name='{}';".format(name)))
    cursor.execute(("commit;"))
 
def modify_task():
    name = raw_input("Enter name of task to modify it's duration")   
    cursor.execute(("delete from tasks where task_name='{}';".format(name)))
    cursor.execute(("commit;"))
    duration = raw_input("Enter new estimated duration of task\n")
    cursor.execute(("insert into tasks(task_name,duration) values('{}', '{}');".format(name, duration)))
    cursor.execute(("commit;"))
       
    
#create_event()
#delete_event("event2")
#modify_event()
#add_task()
#finish_task()
modify_task()

cursor.close();
