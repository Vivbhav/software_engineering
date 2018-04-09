import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def new_event_create():
    class MyWindow(Gtk.Window):
        def __init__(self):
            Gtk.Window.__init__(self, title="Create an event")
            
            self.date_print = Gtk.Label("Date")
            self.add(self.date_print)

    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.set_default_size(800, 1000)
    win.show_all()
    Gtk.main()

new_event_create()
