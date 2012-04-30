from gi.repository import Gtk
from settings import Settings
import gettext
import os.path
from controllers import PhotoRenamer

_ = gettext.gettext

class MainWindow(object):
    def __init__(self):
        self.settings = Settings()
        self.files = []
        builder = Gtk.Builder()
        builder.add_from_file("ui/main.ui")

        handlers = {
            "on_delete_window": Gtk.main_quit,
            "on_show_about": self.show_about,
            "on_open_file": self.open_file,
            "on_rename_file": self.rename_file
        }
        builder.connect_signals(handlers)
        self.textview = builder.get_object("tv_main")
        window = builder.get_object("main_window")
        window.show_all()
        Gtk.main()

    def rename_file(self, *args):
        renamer = PhotoRenamer()
        renamer.file_list = self.files
        renamer.update_targets_from_filelist()
        log_text = _('log-rename-files') + ':\n'
        log_text = log_text + ('-' * len(log_text)) + '\n'
        for target in renamer.targets:
            target.rename()
            log_text = log_text + \
                       target.original_file_name + '\n\t -> ' + \
                       target.renamed_file_name + '\n'
        buffer = Gtk.TextBuffer()
        buffer.set_text(log_text)
        self.textview.set_buffer(buffer)

    def open_file(self, *args):
        file_selector = Gtk.FileChooserDialog(_('select-file'), None, Gtk.FileChooserAction.OPEN)
        file_selector.set_select_multiple(True)
        file_selector.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        file_selector.add_button(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        filter = Gtk.FileFilter()
        filter.set_name('*.jpg')
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.jPG")
        filter.add_pattern("*.jPEG")
        filter.add_pattern("*.jpeg")
        file_selector.add_filter(filter)
        file_selector.run()
        self.files = file_selector.get_filenames()
        buffer = Gtk.TextBuffer()
        if file_selector.get_filename():
            log_text = _('log-selected-files') + ' in ' + os.path.dirname(file_selector.get_filename()) + ':\n'
            log_text = log_text + ('-' * (len(log_text) + 5)) + '\n'
            log_text = log_text + '\n'.join(map(os.path.basename, self.files))
            buffer.set_text(log_text)
            self.textview.set_buffer(buffer)
        file_selector.destroy()


    def show_about(self, *args):
        about_dialog = Gtk.AboutDialog()
        about_dialog.connect("response", lambda d, r: d.destroy())
        about_dialog.set_authors(["Chris Martel"])
        about_dialog.set_comments(_("Rename photo files based on exif data"))
        about_dialog.set_copyright("Copyright (C) 2012 Chris Martel")
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