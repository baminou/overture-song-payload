
from .PayloadObject import PayloadObject
import os
import hashlib

class FilePayload(PayloadObject):

    def __init__(self, file_access=None, file_name=None, md5sum=None, file_type=None, file_size=None, info=None):
        self.file_access = file_access
        self.file_name = file_name
        self.file_md5_sum = md5sum
        self.file_type = file_type
        self.file_size = file_size
        self.info = {} if info==None else info
        return

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

    def set_info(self, info):
        self.info = info
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

    def get_info(self):
        return self.info

    def to_array(self):
        return {
            'fileAccess': self.get_file_access(),
            'fileMd5sum': self.get_file_md5_sum(),
            'fileName': self.get_file_name(),
            'fileType': self.get_file_type(),
            'fileSize': int(self.get_file_size()),
            'info': self.get_info()
        }

    @staticmethod
    def calculate_size(file_path):
        return os.stat(file_path).st_size

    @staticmethod
    def calculate_md5(file_path):
        def md5sum(filename):
            md5 = hashlib.md5()
            with open(filename, 'rb') as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b''):
                    md5.update(chunk)
            return md5.hexdigest()
        return md5sum(file_path)

    @staticmethod
    def retrieve_file_type(fname):
        if fname.endswith('.xml'):
            return 'XML'
        if fname.endswith('.xml.gz'):
            return 'XML'
        if fname.endswith('.bai'):
            return 'BAI'
        if fname.endswith('.bam'):
            return 'BAM'
        if fname.endswith('.fastq'):
            return 'FASTQ'
        if fname.endswith('.fastq.gz'):
            return 'FASTQ'
        if fname.endswith('.fq'):
            return 'FASTQ'
        if fname.endswith('.fq.gz'):
            return 'FASTQ'
        raise Exception('unknown file type for file: %s' % fname)

