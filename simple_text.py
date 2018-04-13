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
import search
import sentiment
from pygame import mixer
import youtube_final
#import text_to_speech

try:
    cnx = MySQLdb.connect("localhost", "root", "vivbhav97", "events")
except:
    cnx = MySQLdb.connect("localhost", "root", "Amritraj26", "events")
cursor = cnx.cursor()

class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        self.state = ("random", 0)
        self.temp = "start"
        self.start = "start"
        self.count = 0 
        Gtk.Window.__init__(self, title="Virtual Personal Assistant", application=app)
        self.set_default_size(300, 450)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        enter_button = Gtk.Button(label="Give command")
        enter_button.connect("clicked", self.enter_clicked)
        self.box.pack_start(enter_button, False, True, 0)

        self.box1 = Gtk.HBox(True, 2)
        scroll = Gtk.ScrolledWindow()
        scroll.set_hexpand(True)
        scroll.set_vexpand(True)
        scroll.set_border_width(5)
        scroll.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.buffer2 = Gtk.TextBuffer()
        self.textview2 = Gtk.TextView(buffer=self.buffer2)
        self.textview2.set_wrap_mode(Gtk.WrapMode.WORD)
        scroll.add(self.textview2)
        self.buffer2.insert_at_cursor("Commands\nCreate event - to create a new event\nModify event - to modify an existing event\nDelete event - to delete an existing event\nSend mail - to send an email\nSentiment Analysis - to perform sentiment analysis on your thoughts\nPoem - to receive the poem of the day\nYoutube - to search anything on youtube\nGoogle - to search anything on google and receive most relevant links along with their initial contents\n")


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
        self.textview = Gtk.TextView(buffer=self.buffer1)
        # wrap the text, if needed, breaking lines in between words
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)

        # textview is scrolled
        scrolled_window.add(self.textview)
    
        self.box1.pack_start(scrolled_window, True, True, 0)
        self.box1.pack_start(scroll, True, True, 0)
        self.box.pack_start(self.box1, True, True, 0)       

        #self.add(scrolled_window)

    def color_to_give(self, widget):
        for i in range(self.count):
            if i % 2:
                tag = self.buffer1.create_tag("green_bg", background="green")
                start_iter = self.buffer1.get_iter_at_line(i)
                end_iter = self.buffer1.get_iter_at_line(i + 1)
                self.buffer1.apply_tag(tag, start_iter, end_iter)                    
                self.buffer1.remove_all_tags(start_iter, end_iter)
            else:
                tag2 = self.buffer1.create_tag("red_bg", background="red")
                start_iter = self.buffer1.get_iter_at_line(i)
                end_iter = self.buffer1.get_iter_at_line(i + 1)
                self.buffer1.apply_tag(tag2, start_iter, end_iter)
                self.buffer1.remove_all_tags(start_iter, end_iter)
        self.count += 2       

    def enter_clicked(self, widget):
        start_iter = self.buffer1.get_start_iter()
        end_iter = self.buffer1.get_end_iter()

        #self.temp = end_iter

        text = self.buffer1.get_text(start_iter, end_iter, True)
    	#print ("i am in funtion")
        #output = self.buffer1.gtk_text_buffer_get_text()
        a = text.strip().split("\n")
        text = a[-1]
        a = text.strip().split("\n")
        text = ""
        for i in a:
            text += str(i)
        print ("start of text")
        print (text)
        print ("end of text")
       
    	#word_list = word_tokenize(string)

	    #Setting up stop_words: words that are redundant.
    	#stop_words = set(stopwords.words('english'))
   
        if self.state[1] == 0 or self.state[1] == 5 or self.state[1] == 12 or self.state[1] == 24 or self.state[1] == 36 or self.state[1] == 42 or self.state[1] == 52:
            print ("called main code")
            self.state = mainCode.main_code(text)

        ## all of this code for creation of event
        if self.state[1] == 4:
            #tag = self.buffer1.create_tag("green_bg", background="green")
            #start_iter = self.buffer1.get_start_iter()
            #end_iter = self.buffer1.get_end_iter()
            #self.buffer1.apply_tag(tag, start_iter, end_iter)
            #self.buffer1.remove_all_tags(start_iter, end_iter)
            self.end_dt = parser.parse(text)
            cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(self.name, self.start_dt, self.end_dt)))
            text_to_speech.speak("inserted your event")
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 5
            self.state = tuple(self.state)
            #color_to_give()

        if self.state[1] == 3:
            #tag = self.buffer1.create_tag("red_bg", background="red")
            #start_iter = self.buffer1.get_start_iter()
            #end_iter = self.buffer1.get_end_iter()
            #self.buffer1.apply_tag(tag, start_iter, end_iter)
            self.start_dt = parser.parse(text)
            self.buffer1.insert_at_cursor("\nPi : insert end time of event\n")
            #self.buffer1.remove_all_tags(start_iter, end_iter)
            text_to_speech.speak("insert end time of event")
            self.state = list(self.state)
            self.state[1] = 4
            self.state = tuple(self.state)
            #color_to_give()

        if self.state[1] == 2:
            #tag = self.buffer1.create_tag("green_bg", background="green")
            #start_iter = self.buffer1.get_start_iter()
            #end_iter = self.buffer1.get_end_iter()
            #self.buffer1.apply_tag(tag, start_iter, end_iter)
            self.name = text
            self.buffer1.insert_at_cursor("\nPi : insert start time of event\n")
            #self.buffer1.remove_all_tags(start_iter, end_iter)
            text_to_speech.speak("insert start time of event")
            self.state = list(self.state)
            self.state[1] = 3
            self.state = tuple(self.state)
            #color_to_give()
        
        if self.state[1] == 1:
            #tag = self.buffer1.create_tag("red_bg", background="red")
            #start_iter = self.buffer1.get_start_iter()
            #end_iter = self.buffer1.get_end_iter()
            #self.buffer1.apply_tag(tag, start_iter, end_iter)
            self.buffer1.insert_at_cursor("\nPi : insert name of event to create\n")
            #self.buffer1.remove_all_tags(start_iter, end_iter)
            text_to_speech.speak("insert name of event")
            self.state = list(self.state)
            self.state[1] = 2
            self.state = tuple(self.state)
            #color_to_give()

        ## all of this code for deletion of event

        if self.state[1] == 11:
            self.name = text    
            cursor.execute(("delete from events_list where event_name='{}';".format(self.name)))
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 0 #12
            self.state = tuple(self.state)

        if self.state[1] == 10:
            self.buffer1.insert_at_cursor("\nPi : Give name of event to delete\n")
            text_to_speech.speak("give name of the event to delete")
            self.state = list(self.state)
            self.state[1] = 11
            self.state = tuple(self.state)

            	
        ## all of this code for modification of event
        if self.state[1] == 23:
            self.end_dt = parser.parse(text)
            cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(self.name, self.start_dt, self.end_dt)))
            cursor.execute(("commit;"))
            self.state = list(self.state)
            self.state[1] = 0 #24
            self.state = tuple(self.state)

        if self.state[1] == 22:
            self.start_dt = parser.parse(text)
            self.buffer1.insert_at_cursor("\nPi : insert new end time of event\n")
            text_to_speech.speak("insert new end time of event")
            self.state = list(self.state)
            self.state[1] = 23
            self.state = tuple(self.state)

        if self.state[1] == 21:
            self.name = text
            cursor.execute(("delete from events_list where event_name='{}';".format(self.name)))
            cursor.execute(("commit;"))
            self.buffer1.insert_at_cursor("\nPi : insert new start time of event\n")
            text_to_speech.speak("insert new start time of event")
            self.state = list(self.state)
            self.state[1] = 22
            self.state = tuple(self.state)
        
        if self.state[1] == 20:
            self.buffer1.insert_at_cursor("\nPi : insert name of event to modify\n")
            text_to_speech.speak("insert name of event to modify")
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
            self.state[1] = 0 #36
            self.state = tuple(self.state)

        if self.state[1] == 34:
            self.username = text
            self.buffer1.insert_at_cursor("\nPi : Enter your email password\n")
            text_to_speech.speak("Enter you email password")
            self.state = list(self.state)
            self.state[1] = 35
            self.state = tuple(self.state)

        if self.state[1] == 33:
            self.msg = text
            self.buffer1.insert_at_cursor("\nPi : Enter your username\n")
            text_to_speech.speak("enter your username")
            self.state = list(self.state)
            self.state[1] = 34
            self.state = tuple(self.state)

        if self.state[1] == 32:
            self.toaddrs = text
            self.buffer1.insert_at_cursor("\Pi : nEnter content of email\n")
            text_to_speech.speak("enter content of email")
            self.state = list(self.state)
            self.state[1] = 33
            self.state = tuple(self.state)

        if self.state[1] == 31:
            self.fromaddr = text
            self.buffer1.insert_at_cursor("\nPi : Enter recipient's email\n")
            text_to_speech.speak("enter recipient's email")
            self.state = list(self.state)
            self.state[1] = 32
            self.state = tuple(self.state)

        if self.state[1] == 30:
            self.buffer1.insert_at_cursor("\nPi : Enter your email\n")
            text_to_speech.speak("enter your email")
            self.state = list(self.state)
            self.state[1] = 31
            self.state = tuple(self.state)
        
        if self.state[1] == 41:
            search.search(text)	
	        #time.sleep(15)
            myfile = open("out.txt", "r")
            data = myfile.read()
            print (data)
            print ("google results printing over")
            self.buffer1.insert_at_cursor(data)
            self.state = list(self.state)
            self.state[1] = 0 #42
            self.state = tuple(self.state)
           
        if self.state[1] == 40:
            self.buffer1.insert_at_cursor("\nPi : Enter what do you want to google\n")
            text_to_speech.speak("I can do it. What do you want me to look for?")
            self.state = list(self.state)
            self.state[1] = 41
            self.state = tuple(self.state)
        
        if self.state[1] == 51:
            out = sentiment.sentiment_analysis(text)
            print ("printing sentiment output")
            print (out)
            print ("end of sentiment out")
            mixer.init()
            #self.buffer1.insert_at_cursor(out)
            if int(out) == 0:
                mixer.music.load('/home/vivek/Desktop/software_engineering/project/hello.mp3')
                mixer.music.play()
            elif int(out) == 1:
                mixer.music.load('/home/vivek/Desktop/software_engineering/project/hello1.mp3')
                mixer.music.play()
            elif int(out) == 2:
                mixer.music.load('/home/vivek/Desktop/software_engineering/project/hello2.mp3')
                mixer.music.play()
            elif int(out) == 3:
                mixer.music.load('/home/vivek/Desktop/software_engineering/project/hello3.mp3')
                mixer.music.play()
            elif int(out) == 4:
                mixer.music.load('/home/vivek/Desktop/software_engineering/project/hello4.mp3')
                mixer.music.play()
            self.state = list(self.state)
            self.state[1] = 0 #52
            self.state = tuple(self.state)
            
        if self.state[1] == 50:
            self.buffer1.insert_at_cursor("\nPi : What are you thinking about\n")
            text_to_speech.speak("Tell me how are you feeling")
            self.state = list(self.state)
            self.state[1] = 51
            self.state = tuple(self.state)
             
        if self.state[1] == 60:
            cursor.execute("select * from events_list order by start_time;")
            rows = [i for i in cursor]
            self.buffer1.insert_at_cursor("\nPi : ")
            for i in rows:
                self.buffer1.insert_at_cursor(str(i[1]) + "\t" + str(i[2]) + "\t" + str(i[3]) + "\n")

        if self.state[1] == 71:
	    a = text.strip().split("#")
	    print (a)
	    para1 = a[0]
	    para2 = a[1]
	    print (para1)
	    print (para2)
            data = youtube_final.youtube(para1, para2)
            self.buffer1.insert_at_cursor(data)
            self.state = list(self.state)
            self.state[1] = 72
            self.state = tuple(self.state)
	
	if self.state[1] == 70:
            self.buffer1.insert_at_cursor("\nPi : What should I search on youtube, Also enter (1) to show all results or (2) to play the most relevant one\n")
            text_to_speech.speak("You got it. Which video?")
            self.state = list(self.state)
            self.state[1] = 71
            self.state = tuple(self.state)
	                 

        if self.state[1] == 5:
            self.buffer1.insert_at_cursor("\nPi : created event\n")
             
            text_to_speech.speak("created event")     
        elif self.state[1] == 12:
            self.buffer1.insert_at_cursor("\nPi : deleted event\n")
            text_to_speech.speak("deleted event")      
        elif self.state[1] == 24:
            self.buffer1.insert_at_cursor("\nPi : modified event\n")
            text_to_speech.speak("modified event")     
        elif self.state[1] == 36:
            self.buffer1.insert_at_cursor("\nPi : email sent\n")
            text_to_speech.speak("email sent") 
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
