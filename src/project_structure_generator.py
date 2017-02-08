"""Project structure generator module."""
from pathlib import Path
from src.file_folder_creators import create_folder

class ProjectStructureGenerator(object):
    """Project structure generator class."""

    @staticmethod
    def generate(root_path, project_name):
        """Generates the project folder structure."""
        project_base = root_path + '/' + project_name
        src_path = project_base + '/src'
        tests_path = project_base + '/tests'
        create_folder(project_base)
        create_folder(src_path)
        Path(src_path + '/__init__.py').touch()
        create_folder(tests_path)
        Path(tests_path + '/__init__.py').touch()
