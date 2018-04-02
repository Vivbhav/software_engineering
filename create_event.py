import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Choose an Option")
        
        def b1_click(self, widget):
            print("View Calender")

        def b2_click(self, widget):
            print("Send emails")

        grid = Gtk.Grid()
        self.add(grid)
        
        button1 = Gtk.Button(label="View Calender")
        button2 = Gtk.Button(label="Send Emails")
        button1.set_size_request(50, 100)
        button2.set_size_request(50, 100)

        button1.connect("clicked", b1_click)
        button2.connect("clicked", b2_click)        

        grid.add(button1)
        #grid.attach(button2, 1, 0, 4, 4)
        grid.add(button2)

win = GridWindow()
win.set_default_size(800, 1000)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
