#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS
from windows import MainWindow

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def main():
    w = MainWindow()

    return 0

if __name__ == '__main__':
    main()
