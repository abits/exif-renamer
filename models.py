from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

class Photo():
    def __init__(self):
        self.original_base_dir = ''
        self.original_file_name = ''
        self.renamed_file_name = ''
        self.raw_exif_data = {}
        self.date = datetime()
        self.dirty = false

    def rename(self):
        pass

    def rename_and_save(self):
        self.rename()
        pass

    def update_exif_data(self):
        pass

    def get_exif(fn):
        return_value = {}
        i = Image.open(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            return_value[decoded] = value
        return return_value
