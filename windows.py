from gi.repository import Gtk
from settings import Settings
import gettext

_ = gettext.gettext

class DirChooser():
    def __init__(self):
        self.dirchooser_dialog = Gtk.Builder()
        self.dirchooser_dialog.add_from_file("ui/dirchooser.ui")
        self.dirchooser_dialog.connect_signals(self)
        self.dialog = self.dirchooser_dialog.get_object('dirchooserdialog')
        self.checkbutton_recursive = self.dirchooser_dialog.get_object('checkbutton_recursive')
        self.directory = None
        self.recursive = self.checkbutton_recursive.get_active()

    def quit(self):
        self.dialog.destroy()

    def on_button_cancel_clicked(self, *args):
        self.quit()

    def on_button_ok_clicked(self, *args):
        self.recursive = self.checkbutton_recursive.get_active()
        self.directory = self.dialog.get_filename()


class MainWindow(object):
    def __init__(self):
        self.settings = Settings()
        builder = Gtk.Builder()
        builder.add_from_file("ui/main.ui")

        handlers = {
            "on_delete_window": Gtk.main_quit,
            "on_show_about": self.show_about,
            "on_open_directory": self.open_directory,
            }
        builder.connect_signals(handlers)
        window = builder.get_object("main_window")
        window.show_all()
        Gtk.main()

    def open_directory(self, *args):
        dir_selector = DirChooser()
        dir_selector.checkbutton_recursive.set_active(
            self.settings.recursive)
        result = dir_selector.dialog.run()
        top_directory = dir_selector.directory
        self.settings.recursive = dir_selector.recursive
        dir_selector.quit()
        if top_directory is not None:
            pass

    def show_about(self, *args):
        print args
        about_dialog = Gtk.AboutDialog()
        about_dialog.connect("response", lambda d, r: d.destroy())
        about_dialog.set_authors(["Chris Martel"])
        about_dialog.set_comments(_("Rename photo files based on exif data"))
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
        about_dialog.set_name("ExifRenamer")
        about_dialog.set_version("0.0.1")
        about_dialog.set_website("https://github.com/abits/exif-renamer")
        about_dialog.run()