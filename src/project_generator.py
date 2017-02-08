"""Project generator module."""
from src.project_config import ProjectConfiguration
from src.project_structure_generator import ProjectStructureGenerator
from src.metadata_generator import MetadataGenerator
from src.setup_generator import SetupGenerator
from src.tox_generator import ToxGenerator
from src.gitignore_generator import GitignoreGenerator
from src.readme_generator import ReadmeGenerator
from src.license_generator import LicenseGenerator
from src.noserc_generator import NosercGenerator

class ProjectGenerator(object):
    """Project generator class."""

    def __init__(self, configuration):
        if not isinstance(configuration, ProjectConfiguration):
            raise ValueError('configuration is not of type ProjectConfiguration')
        self.configuration = configuration

    def generate(self, root_path):
        """Generates the project folder structure and files."""
        ProjectStructureGenerator.generate(root_path, self.configuration.metadata['NAME'])
        MetadataGenerator.generate(self.configuration.metadata, root_path + "/metadata.py")
        SetupGenerator.generate(root_path + "/setup.py")
        ToxGenerator.generate(root_path + "/.tox.ini")
        GitignoreGenerator.generate(root_path + "/.gitignore")
        ReadmeGenerator.generate(root_path + "/README.md", self.configuration.readme)
        LicenseGenerator.generate(root_path + "/LICENSE", self.configuration.license)
        NosercGenerator.generate(root_path + "/.noserc")
