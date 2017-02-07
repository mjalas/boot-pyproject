import os
from src.file_folder_creators import create_folder

class ProjectStructureGenerator(object):

    @staticmethod
    def generate(root_path, project_name):
        """Generates the project folder structure."""
        project_base = root_path + "/" + project_name
        create_folder(project_base)
        create_folder(project_base + "/src")
        create_folder(project_base + "/tests")
