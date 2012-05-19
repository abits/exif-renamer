import os

class Settings():
    user_data = '/usr/share/exif-renamer'
    ui_data = user_data + os.sep + 'ui'
    recursive = True
    rename_scheme = 'YYYY_mm_DD_HH_MM_SS'

