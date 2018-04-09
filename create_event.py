import gi
from func import view_calender_click
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def view_calender_main_click():
    view_calender_click()

class GridWindow(Gtk.Window):
    
    def b1_click(self, widget):
        view_calender_main_click()

    def b2_click(self, widget):
        but_click()

    def __init__(self):
        Gtk.Window.__init__(self, title="Choose an Option")
        
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.Box()
        #self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('View Calendar'))
        self.notebook.append_page(self.page1, Gtk.Label('Calendar'))

        self.page2 = Gtk.Box()
        #self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('Emails'))
        self.notebook.append_page(self.page2, Gtk.Label('Send Emails'))

        """grid = Gtk.Grid()
        self.add(grid)
        
        button1 = Gtk.Button(label="View Calender")
        button2 = Gtk.Button(label="Send Emails")
        button1.set_size_request(50, 100)
        button2.set_size_request(50, 100)

        button1.connect("clicked", self.b1_click)
        button2.connect("clicked", self.b2_click)        

        
        
        grid.add(button1)
        #grid.attach(button2, 1, 0, 4, 4)
        grid.add(button2)"""

win = GridWindow()
win.set_default_size(800, 1000)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
