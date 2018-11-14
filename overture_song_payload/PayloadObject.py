
import json

class PayloadObject():
    def to_json(self):
        return json.dumps(self.to_array())

    def to_json_file(self, output_file):
        with open(output_file, 'w') as output_file:
            json.dump(self.to_array(), output_file,indent=4,sort_keys=True)

    def to_array(self):
        raise NotImplementedError("Cannot be converted to array, since not implemented.")