
from .PayloadObject import PayloadObject
import jsonschema
import urllib
import json

class SongPayload(PayloadObject):

    def __init__(self, analysis_id=None, analysis_type=None, experiment_payload=None, study=None, sample_payloads=[], file_payloads=[], info={}):
        self.file_payloads = file_payloads
        self.info = info
        self.analysis_id = analysis_id
        self.analysis_type = analysis_type
        self.experiment_payload = experiment_payload
        self.sample_payloads = sample_payloads
        self.study = study

    def set_analysis_id(self, analysis_id=None):
        self.analysis_id = analysis_id
        return

    def set_analysis_type(self, analysis_type=None):
        self.analysis_type = analysis_type
        return

    def set_experiment_payload(self, experiment_payload):
        self.experiment_payload = experiment_payload
        return

    def set_sample_payloads(self, sample_payloads):
        self.sample_payloads = sample_payloads
        return

    def add_sample_payload(self, sample_payload):
        self.sample_payloads.append(sample_payload)
        return

    def set_file_payloads(self, file_payloads):
        self.file_payloads = file_payloads
        return

    def set_study_id(self, study_id):
        self.study_id = study_id
        return

    def add_file_payload(self, file_payload):
        self.file_payloads.append(file_payload)
        return

    def get_file_payloads(self):
        return self.file_payloads

    def get_study(self):
        return self.study

    def get_sample_payloads(self):
        return self.sample_payloads

    def get_analysis_id(self):
        return self.analysis_id

    def get_analysis_type(self):
        return self.analysis_type

    def get_experiment_payload(self):
        return self.experiment_payload

    def add_info(self, key, info):
        self.info[key] = info
        return

    def get_info(self):
        return self.info

    def _get_schema(self):
        url = "https://raw.githubusercontent.com/overture-stack/SONG/develop/song-server/src/main/resources/schemas/sequencingRead.json"
        response = urllib.request.urlopen(url)
        return json.loads(response.read())

    def validate(self):
        jsonschema.validate(self.to_json(),self._get_schema())

    def to_array(self):
        _dict = {
            'analysisId': self.get_analysis_id(),
            'analysisType': self.get_analysis_type(),
            'experiment': self.get_experiment_payload().to_array(),
            'study': self.get_study(),
            'info': self.get_info()
        }

        _dict['file'] = []
        for file_payload in self.get_file_payloads():
            _dict['file'].append(file_payload.to_array())

        _dict['sample'] = []
        for sample_payload in self.get_sample_payloads():
            _dict['sample'].append(sample_payload.to_array())

        return _dict