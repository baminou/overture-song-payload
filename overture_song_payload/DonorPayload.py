
from .PayloadObject import PayloadObject

class DonorPayload(PayloadObject):

    def __init__(self, donor_gender=None, donor_submitter_id=None, study_id=None, info=None):
        self.donor_gender = donor_gender
        self.donor_submitter_id = donor_submitter_id
        self.study_id = study_id
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

    def set_study_id(self, study_id):
        self.study_id = study_id

    def get_donor_gender(self):
        return self.donor_gender

    def get_donor_submitter_id(self):
        return self.donor_submitter_id

    def get_info(self):
        return self.info

    def get_study_id(self):
        return self.study_id

    def to_array(self):
        return {
            'donorGender': self.get_donor_gender(),
            'donorSubmitterId': self.get_donor_submitter_id(),
            'studyId': self.get_study_id(),
            'info':self.get_info()
        }
