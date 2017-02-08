"""Project generator module."""
from src.project_config import ProjectConfiguration
from src.project_structure_generator import ProjectStructureGenerator
from src.metadata_generator import MetadataGenerator

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
        