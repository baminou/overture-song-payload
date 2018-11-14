
from .PayloadObject import PayloadObject

class FilePayload(PayloadObject):

    def __init__(self, file_access=None, file_name=None, md5sum=None, file_type=None, file_size=None):
        self.file_access = file_access
        self.file_name = file_name
        self.file_md5_sum = md5sum
        self.file_type = file_type
        self.file_size = file_size

    def set_file_access(self, file_access):
        self.file_access = file_access
        return

    def set_file_md5_sum(self, md5sum):
        self.file_md5_sum = md5sum
        return

    def set_file_name(self, name):
        self.file_name = name
        return

    def set_file_size(self, size):
        self.file_size = size
        return

    def set_file_type(self, type):
        self.file_type = type
        return

    def get_file_access(self):
        return self.file_access

    def get_file_md5_sum(self):
        return self.file_md5_sum

    def get_file_name(self):
        return self.file_name

    def get_file_size(self):
        return str(self.file_size)

    def get_file_type(self):
        return self.file_type

    def to_array(self):
        return {
            'fileAccess': self.get_file_access(),
            'fileMd5sum': self.get_file_md5_sum(),
            'fileName': self.get_file_name(),
            'fileType': self.get_file_type(),
            'fileSize': int(self.get_file_size())
        }
