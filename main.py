#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS
from gi.repository import Gtk


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def main():
    builder = Gtk.Builder()
    builder.add_from_file("gui/main.ui")

    handlers = {
        "onDeleteWindow": Gtk.main_quit,
        }
    builder.connect_signals(handlers)
    window = builder.get_object("window1")
    window.show_all()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()
