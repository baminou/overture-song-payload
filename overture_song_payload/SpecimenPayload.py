
from .PayloadObject import PayloadObject

class SpecimenPayload(PayloadObject):

    def __init__(self, specimen_class=None, specimen_submitter_id=None, specimen_type=None, info=None):
        self.specimen_class = specimen_class
        self.specimen_submitter_id = specimen_submitter_id
        self.specimen_type = specimen_type
        self.info = {} if info==None else info

    def set_specimen_class(self, specimen_class):
        self.specimen_class = specimen_class
        return

    def set_specimen_submitter_id(self, specimen_submitter_id):
        self.specimen_submitter_id = specimen_submitter_id
        return

    def set_specimen_type(self, specimen_type):
        self.specimen_type = specimen_type
        return

    def set_info(self, info):
        self.info = info

    def get_specimen_class(self):
        return self.specimen_class

    def get_specimen_submitter_id(self):
        return self.specimen_submitter_id

    def get_specimen_type(self):
        return self.specimen_type

    def get_info(self):
        return self.info

    def to_array(self):
        return {
            'specimenClass': self.get_specimen_class(),
            'specimenSubmitterId': self.get_specimen_submitter_id(),
            'specimenType': self.get_specimen_type(),
            'info': self.get_info()
        }