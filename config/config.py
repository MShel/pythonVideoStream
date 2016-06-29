import os
from configparser import ConfigParser


class Config:

    raw_config_object = None

    FILES_SECTION = ''

    COMPRESSION_SECTION = ''

    TRANSPORT_SECTION = ''

    ENCRYPTION_SECTION = ''

    def __init__(self, filename: str):
        self.raw_config_object = self.get_config_object(filename)
        self.COMPRESSION_SECTION = 'COMPRESSION'
        self.TRANSPORT_SECTION = 'TRANSPORT'
        self.ENCRYPTION_SECTION = 'ENCRYPTION'
        self.FILES_SECTION = 'FILES'
        self.validate()

    '''
    exceptions:
        ValueError: (if tmp directory is not writable)
    '''

    def validate(self):
        if not os.access(self.raw_config_object[self.FILES_SECTION]['tmp_directory'], os.W_OK):
            raise ValueError('Tmp directory is not writable')

    def get_config_object(self, filename: str) -> dict:
        config_parser = ConfigParser()
        config_parser.read(filename)
        return config_parser
