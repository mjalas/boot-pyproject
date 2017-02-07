"""Metadata file generator module."""

class MetadataGenerator(object):
    """Metadata file generator class."""

    @staticmethod
    def generate(metadata, file_path):
        """Generates the metadata file."""
        with open(file_path, 'w') as stream:
            for key, value in metadata.iter():
                stream.write(key + "=" + value)
