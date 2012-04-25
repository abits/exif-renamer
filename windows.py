from gi.repository import Gtk
import gettext
_ = gettext.gettext

class MainWindow(object):
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("ui/main.ui")

        handlers = {
            "on_delete_window": Gtk.main_quit,
            "on_show_about": self.show_about
            }
        builder.connect_signals(handlers)
        window = builder.get_object("main_window")
        window.show_all()
        Gtk.main()

    def show_about(self, args):
        print args
        about_dialog = Gtk.AboutDialog()
        about_dialog.connect("response", lambda d, r: d.destroy())
        about_dialog.set_authors(["Chris Martel"])
        about_dialog.set_comments(_("Liedtexte finden & in MP3 schreiben"))
        about_dialog.set_copyright("Copyright (C) 2010 Chris Martel")
        about_dialog.set_wrap_license(True)
        about_dialog.set_license("This program is free software; " +
                                 "you can redistribute it and/or modify it " +
                                 "under the terms of the GNU General Public License as published by " +
                                 "the Free Software Foundation; either version 3 of the License, or " +
                                 "(at your option) any later version. " +
                                 "This program is distributed in the hope that it will be useful, " +
                                 "but WITHOUT ANY WARRANTY; without even the implied warranty of " +
                                 "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU " +
                                 "General Public License for more details. " +
                                 "\n" +
                                 "You should have received a copy of the GNU General Public License " +
                                 "along with this program; if not, see <http://www.gnu.org/licenses/>.")
        about_dialog.set_name("LyricsGrabber")
        about_dialog.set_version("0.1.3")
        about_dialog.set_website("http://lyricsgrabber.sourceforge.net/")
        about_dialog.run()