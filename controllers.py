from models import *
import os
import shutil

class PhotoRenamer():
    backup_dir = 'backup_rename'
    base_dir = ''
    targets = []
    file_list = []

    def get_backup_path(self, target):
        self.base_dir = target.original_base_dir
        return os.path.join(self.base_dir, self.backup_dir)

    def rename_batch(self, targets):
        for target in targets:
            self.rename_single(target)

    def rename_single(self, target):
        target_backup_dir = self.get_backup_path(target)
        print target_backup_dir
        try:
            os.mkdir(target_backup_dir)
        except OSError:
            print target_backup_dir + " already existed."
        shutil.copy(target.get_original_path(), target_backup_dir)
        os.rename(target.get_original_path(), target.get_rename_path())

    def build_photos(self, targets):
        pass

    def update_targets_from_filelist(self):
        for file_name in self.file_list:
            photo = Photo(file_name)
            photo.update_exif_data()
            self.targets.append(photo)
