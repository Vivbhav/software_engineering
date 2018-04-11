import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
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
        self.buffer1.insert_at_cursor("\nhi, how are you\n")        


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
