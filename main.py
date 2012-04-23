#!bin/env python

from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

if __name__ == '__main__':
    fn = open('/home/chm/Bilder/2010-07-17/IMG_2710.JPG', 'r')
    print get_exif(fn)
