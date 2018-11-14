
from .DonorPayload import DonorPayload

class SamplePayload(DonorPayload):

    def __init__(self, donor_payload, sample_submitter_id, sample_type, specimen_payload):
        self.donor_payload = donor_payload
        self.sample_submitter_id = sample_submitter_id
        self.sample_type = sample_type
        self.specimen_payload = specimen_payload

    def set_sample_submitter_id(self, sample_submitter_id):
        self.sample_submitter_id = sample_submitter_id
        return

    def set_sample_type(self, sample_type):
        self.sample_type = sample_type
        return

    def set_specimen_payload(self, specimen_payload):
        self.specimen_payload = specimen_payload
        return

    def set_donor_payload(self, donor_payload):
        self.donor_payload = donor_payload
        return

    def get_sample_submitter_id(self):
        return self.sample_submitter_id

    def get_sample_type(self):
        return self.sample_type

    def get_specimen_payload(self):
        return self.specimen_payload

    def get_donor_payload(self):
        return self.donor_payload

    def to_array(self):
        return {
            'sampleSubmitterId': self.get_sample_submitter_id(),
            'sampleType': self.get_sample_type(),
            'specimen': self.get_specimen_payload().to_array(),
            'donor': self.donor_payload.to_array()
        }