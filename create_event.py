import gi
from func import new_event_create
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):
    
    def new_event_clicked(self, widget):     
        disp = "Display this"
        self.lab.set_text(disp) 
        new_event_create() 

    def __init__(self):
        Gtk.Window.__init__(self, title="Choose an Option")
        
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.Grid()
        #self.page1.set_border_width(10)
        new_event_b= Gtk.ToggleButton(label="Create new event")
        delete_event_b = Gtk.Button(label="Delete an event")
        view_event_b = Gtk.Button(label="View events")
        
        self.lab = Gtk.Label()
        self.empty_lab = Gtk.Label()

        self.page1.add(new_event_b)
        self.page1.attach(delete_event_b, 1, 0, 1, 1)
        self.page1.attach(view_event_b, 2, 0, 1, 1)
        self.page1.attach(self.lab, 0, 1, 1, 1)
        

        new_event_b.connect("toggled", self.new_event_clicked)

        self.notebook.append_page(self.page1, Gtk.Label('Calendar'))

        self.page2 = Gtk.Box()
        #self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('Emails'))
        self.notebook.append_page(self.page2, Gtk.Label('Send Emails'))

win = GridWindow()
win.set_default_size(800, 1000)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
