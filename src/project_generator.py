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
        project_root = root_path + "/" + self.configuration.metadata['NAME']
        ProjectStructureGenerator.generate(project_root)
        MetadataGenerator.generate(self.configuration.metadata, project_root + "/metadata.py")
        SetupGenerator.generate(project_root + "/setup.py")
        ToxGenerator.generate(project_root + "/.tox.ini")
        GitignoreGenerator.generate(project_root + "/.gitignore")
        ReadmeGenerator.generate(project_root + "/README.md", self.configuration.readme)
        LicenseGenerator.generate(project_root + "/LICENSE", self.configuration.license)
        NosercGenerator.generate(project_root + "/.noserc")
