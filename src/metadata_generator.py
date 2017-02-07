"""Metadata file generator module."""
import os

class MetadataGenerator(object):
    """Metadata file generator class."""

    @staticmethod
    def generate(metadata, file_path):
        """Generates the metadata file."""
        if not os.path.exists(file_path):
            with open(file_path, 'w') as stream:
                for key, value in metadata.iter():
                    stream.write(key + "=" + value)
