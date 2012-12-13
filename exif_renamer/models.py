from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from settings import Settings
import ConfigParser
import os

class Photo():
    def __init__(self, file_name):
        self.original_base_dir = os.path.dirname(file_name)
        self.original_file_name = os.path.basename(file_name)
        self.original_file_name_noext = os.path.splitext(self.original_file_name)[0]
        self.renamed_file_name = ''
        self.raw_exif_data = {}
        self.date = None
        self.dirty = False

    def rename(self):
        extension = 'jpg'
        self.renamed_file_name = \
            '{:02d}{:02d}{:02d}_{:02d}{:02d}_{:s}.{:s}'.format(
                self.date.year,
                self.date.month,
                self.date.day,
                self.date.hour,
                self.date.minute,
                self.original_file_name_noext,
                extension)

    def rename_and_save(self):
        self.rename()

    def get_original_path(self):
        return os.path.join(self.original_base_dir, self.original_file_name)

    def get_rename_path(self):
        return os.path.join(self.original_base_dir, self.renamed_file_name)

    def update_exif_data(self):
        self.raw_exif_data = self.get_exif(self.get_original_path())
        #print self.raw_exif_data
        config = ConfigParser.ConfigParser()
        ini_file = os.path.join(Settings.user_data, 'manufacturers', self.raw_exif_data['Make'] + '.ini')
        #print ini_file
        config.read(ini_file)
        ini_section = self.raw_exif_data['Model']
        exif_index = config.get(ini_section, 'datetimeoriginal')
        exif_timestamp = config.get(ini_section, exif_index)
        format_string = '%Y:%m:%d %H:%M:%S'
        self.date =  datetime.strptime(self.raw_exif_data[exif_timestamp], format_string)

    def get_exif(self, file_name):
        return_value = {}
        i = Image.open(file_name)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            return_value[decoded] = value
        return return_value
