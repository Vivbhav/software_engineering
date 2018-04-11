import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from dateutil import parser
import mainCode
import MySQLdb
import time
import smtplib

cnx = MySQLdb.connect("localhost", "root", "vivbhav97", "events")
cursor = cnx.cursor()

class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        self.state = ("random", 0)
        Gtk.Window.__init__(self, title="TextView Example", application=app)
        self.set_default_size(300, 450)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        enter_button = Gtk.Button(label="Give command")
        enter_button.connect("clicked", self.enter_clicked)
        self.box.pack_start(enter_button, False, True, 0)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)

        # a scrollbar for the child widget (that is going to be the textview)
        scrolled_window.set_border_width(5)
        # we scroll only if needed
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        # a text buffer (stores text)
        self.buffer1 = Gtk.TextBuffer()

        # a textview (displays the buffer)
        textview = Gtk.TextView(buffer=self.buffer1)
        # wrap the text, if needed, breaking lines in between words
        textview.set_wrap_mode(Gtk.WrapMode.WORD)

        # textview is scrolled
        scrolled_window.add(textview)

        self.box.pack_start(scrolled_window, True, True, 0)       

        #self.add(scrolled_window)

    def enter_clicked(self, widget):
        start_iter = self.buffer1.get_start_iter()
        end_iter = self.buffer1.get_end_iter()
        text = self.buffer1.get_text(start_iter, end_iter, True)
    	#print ("i am in funtion")
        #output = self.buffer1.gtk_text_buffer_get_text()
        print (text)
    	#word_list = word_tokenize(string)

	    #Setting up stop_words: words that are redundant.
    	#stop_words = set(stopwords.words('english'))
   
        if self.state[1] == 0: 
            self.state = mainCode.main_code(text)

        ## all of this code for creation of event
        if self.state[1] == 4:
            self.end_dt = parser.parse(text)
            cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(self.name, self.start_dt, self.end_dt)))
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 5
            self.state = tuple(self.state)

        if self.state[1] == 3:
            self.start_dt = parser.parse(text)
            self.buffer1.insert_at_cursor("\ninsert end time of event\n")
            self.state = list(self.state)
            self.state[1] = 4
            self.state = tuple(self.state)

        if self.state[1] == 2:
            self.name = text
            self.buffer1.insert_at_cursor("\ninsert start time of event\n")
            self.state = list(self.state)
            self.state[1] = 3
            self.state = tuple(self.state)
        
        if self.state[1] == 1:
            self.buffer1.insert_at_cursor("\ninsert name of event\n")
            self.state = list(self.state)
            self.state[1] = 2
            self.state = tuple(self.state)

        ## all of this code for deletion of event

        if self.state[1] == 11:
            self.name = text    
            cursor.execute(("delete from events_list where event_name='{}';".format(self.name)))
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 12
            self.state = tuple(self.state)

        if self.state[1] == 10:
            self.buffer1.insert_at_cursor("\nGive name of event to delete\n")
            self.state = list(self.state)
            self.state[1] = 11
            self.state = tuple(self.state)

            	
        ## all of this code for modification of event
        if self.state[1] == 23:
            self.end_dt = parser.parse(text)
            cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(self.name, self.start_dt, self.end_dt)))
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 24
            self.state = tuple(self.state)

        if self.state[1] == 22:
            self.start_dt = parser.parse(text)
            self.buffer1.insert_at_cursor("\ninsert new end time of event\n")
            self.state = list(self.state)
            self.state[1] = 23
            self.state = tuple(self.state)

        if self.state[1] == 21:
            self.name = text
            self.buffer1.insert_at_cursor("\ninsert new start time of event\n")
            self.state = list(self.state)
            self.state[1] = 22
            self.state = tuple(self.state)
        
        if self.state[1] == 20:
            self.buffer1.insert_at_cursor("\ninsert name of event to modify\n")
            self.state = list(self.state)
            self.state[1] = 21
            self.state = tuple(self.state)
        
        ## all this code to send email

        if self.state[1] == 35:
            self.password = text
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.fromaddr, self.toaddrs, self.msg)
            server.quit()
            self.state = list(self.state)
            self.state[1] = 36
            self.state = tuple(self.state)

        if self.state[1] == 34:
            self.username = text
            self.buffer1.insert_at_cursor("\nEnter your email password\n")
            self.state = list(self.state)
            self.state[1] = 35
            self.state = tuple(self.state)

        if self.state[1] == 33:
            self.msg = text
            self.buffer1.insert_at_cursor("\nEnter your username\n")
            self.state = list(self.state)
            self.state[1] = 34
            self.state = tuple(self.state)

        if self.state[1] == 32:
            self.toaddrs = text
            self.buffer1.insert_at_cursor("\nEnter content of email\n")
            self.state = list(self.state)
            self.state[1] = 33
            self.state = tuple(self.state)

        if self.state[1] == 31:
            self.fromaddr = text
            self.buffer1.insert_at_cursor("\nEnter email to send email to\n")
            self.state = list(self.state)
            self.state[1] = 32
            self.state = tuple(self.state)

        if self.state[1] == 30:
            self.buffer1.insert_at_cursor("\nEnter email id from where to send email\n")
            self.state = list(self.state)
            self.state[1] = 31
            self.state = tuple(self.state)
            

        if self.state[1] == 5:
            self.buffer1.insert_at_cursor("\ncreated event\n")      
        elif self.state[1] == 12:
            self.buffer1.insert_at_cursor("\ndeleted event\n")      
        elif self.state[1] == 24:
            self.buffer1.insert_at_cursor("\nmodified event\n")     
        elif self.state[1] == 36:
            self.buffer1.insert_at_cursor("\nemail sent\n")     
        elif self.state[1] == 0:
            self.buffer1.insert_at_cursor(self.state[0])      
        #else:
        #    self.buffer1.insert_at_cursor("garbage print")      
				

    #self.buffer1.insert_at_cursor("\nhi, how are you\n")        


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)	
