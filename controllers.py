from models import *

class PhotoRenamer():
    targets = []
    file_list = []

    def rename_batch(self, targets):
        pass

    def rename_single(self, target):
        pass

    def build_photos(self, targets):
        pass

    def update_targets_from_filelist(self):
        for file_name in self.file_list:
            photo = Photo(file_name)
            photo.update_exif_data()
            self.targets.append(photo)
