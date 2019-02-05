
from .PayloadObject import PayloadObject

class ExperimentPayload(PayloadObject):

    def __init__(self, aligned=None, reference_genome=None, library_strategy=None, paired_end=None, info=None):
        self.aligned = aligned
        self.reference_genome = reference_genome
        self.library_strategy = library_strategy
        self.paired_end = paired_end
        self.info = {} if info==None else info

    def set_aligned(self, aligned=None):
        self.aligned = aligned
        return

    def set_library_strategy(self, library_strategy=None):
        self.library_strategy = library_strategy
        return

    def set_reference_genome(self, reference_genome=None):
        self.reference_genome = reference_genome
        return

    def set_info(self, info):
        self.info = info
        return

    def set_paired_end(self, paired_end):
        self.paired_end = paired_end
        return

    def get_aligned(self):
        return self.aligned

    def get_library_strategy(self):
        return self.library_strategy

    def get_reference_genome(self):
        return self.reference_genome

    def get_info(self):
        return self.info

    def get_paired_end(self):
        return self.paired_end

    def to_array(self):
        return {
            'aligned': self.aligned,
            'libraryStrategy': self.library_strategy,
            'referenceGenome': self.reference_genome,
            'pairedEnd': self.get_paired_end(),
            'info': self.info
        }
