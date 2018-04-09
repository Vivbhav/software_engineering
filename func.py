import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ComboBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Creating new event")

        date_label = Gtk.Label("Date")
        #self.add(date_label)

        self.set_border_width(10)

        date_list= Gtk.ListStore(int)
        dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        for date in dates:
            date_list.append([date])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        date_combo = Gtk.ComboBox.new_with_model_and_entry(date_list)
        date_combo.connect("changed", self.on_date_combo_changed)
        date_combo.set_entry_text_column(1)
        vbox.pack_start(date_label, False, False, 0)
        vbox.pack_start(date_combo, False, False, 0)

        country_store = Gtk.ListStore(str)
        countries = ["Austria", "Brazil", "Belgium", "France", "Germany",
            "Switzerland", "United Kingdom", "United States of America",
            "Uruguay"]
        for country in countries:
            country_store.append([country])

        country_combo = Gtk.ComboBox.new_with_model(country_store)
        country_combo.connect("changed", self.on_country_combo_changed)
        renderer_text = Gtk.CellRendererText()
        country_combo.pack_start(renderer_text, True)
        country_combo.add_attribute(renderer_text, "text", 0)
        vbox.pack_start(country_combo, False, False, True)

        currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
            "Russian Ruble", "Mexican peso", "Swiss franc"]
        currency_combo = Gtk.ComboBoxText()
        currency_combo.set_entry_text_column(0)
        currency_combo.connect("changed", self.on_currency_combo_changed)
        for currency in currencies:
            currency_combo.append_text(currency)

        vbox.pack_start(currency_combo, False, False, 0)

        self.add(vbox)

    def on_date_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, date = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, date))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    def on_country_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            country = model[tree_iter][0]
            print("Selected: country=%s" % country)

    def on_currency_combo_changed(self, combo):
        text = combo.get_active_text()
        if text is not None:
            print("Selected: currency=%s" % text)

win = ComboBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.set_default_size(800, 1000)
win.show_all()
Gtk.main()

