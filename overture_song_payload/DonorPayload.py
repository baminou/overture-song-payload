
from .PayloadObject import PayloadObject

class DonorPayload(PayloadObject):

    def __init__(self, donor_gender=None, donor_submitter_id=None, info=None):
        self.donor_gender = donor_gender
        self.donor_submitter_id = donor_submitter_id
        self.info = {} if info==None else info

    def set_donor_gender(self, donor_gender):
        self.donor_gender = donor_gender
        return

    def set_donor_submitter_id(self, donor_submitter_id):
        self.donor_submitter_id = donor_submitter_id
        return

    def set_info(self, info):
        self.info = info
        return

    def get_donor_gender(self):
        return self.donor_gender

    def get_donor_submitter_id(self):
        return self.donor_submitter_id

    def get_info(self):
        return self.info

    def to_array(self):
        return {
            'donorGender': self.get_donor_gender(),
            'donorSubmitterId': self.get_donor_submitter_id(),
            'info':self.get_info()
        }
