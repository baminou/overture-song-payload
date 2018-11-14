
from .PayloadObject import PayloadObject

class DonorPayload(PayloadObject):

    def __init__(self, donor_gender=None, donor_submitter_id=None):
        self.donor_gender = donor_gender
        self.donor_submitter_id = donor_submitter_id

    def set_donor_gender(self, donor_gender):
        self.donor_gender = donor_gender
        return

    def set_donor_submitter_id(self, donor_submitter_id):
        self.donor_submitter_id = donor_submitter_id
        return

    def get_donor_gender(self):
        return self.donor_gender

    def get_donor_submitter_id(self):
        return self.donor_submitter_id

    def to_array(self):
        return {
            'donorGender': self.get_donor_gender(),
            'donorSubmitterId': self.get_donor_submitter_id()
        }
