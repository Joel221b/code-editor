import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
gi.require_version("GtkSource", "3.0")
from gi.repository import GtkSource

from settings import config


class App:
	def __init__(self):
		self.window = Gtk.Window(title = config["title"])
		self.window.set_default_size(700, 700)
		self.window.connect("destroy", Gtk.main_quit)

		self.header_bar = Gtk.HeaderBar(title = config["title"])
		self.header_bar.set_show_close_button(config["set_show_close_button"])
		self.header_bar.set_subtitle("App.py")

		self.view = GtkSource.View()
		self.view.modify_font(Pango.FontDescription("monospace 12"))
		self.view.set_show_line_numbers(config["show_line_numbers"])
		self.view.set_show_line_marks(config["show_line_marks"])

		self.scrolled = Gtk.ScrolledWindow()
		self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		self.scrolled.add(self.view)

	def loadHeaderBar(self):
		self.window.set_titlebar(self.header_bar)

	def loadViews(self):
		self.window.add(self.scrolled)

	def run(self):
		self.window.show_all()
		Gtk.main()


if __name__ == "__main__":
	app = App()
	app.loadViews()
	app.run()