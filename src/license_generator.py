"""License file generator module."""
from pathlib import Path
from src.license_templates import MIT_LICENSE_TEMPLATE, GPL3_LICENSE_TEMPLATE

class LicenseGenerator(object):
    """License file generator class."""

    @staticmethod
    def generate(file_path, license_metadata):
        """Generates the LICENSE file for the project."""
        if license_metadata['file'] == 'MIT':
            with open(file_path, 'w') as stream:
                content = MIT_LICENSE_TEMPLATE
                if 'year' in license_metadata:
                    content = content.replace('<year>', license_metadata['year'])
                if 'owner' in license_metadata:
                    content = content.replace('<owner>', license_metadata['owner'])
                stream.write(content)
        elif license_metadata['file'] == 'GPL3':
            with open(file_path, 'w') as stream:
                stream.write(GPL3_LICENSE_TEMPLATE)
        else:
            Path(file_path).touch()
