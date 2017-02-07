from unittest import TestCase
import json
import yaml
import os
from tests.test_helpers import test_configuration, create_project_conf_file, remove_project_conf_file
from src.project_generator import ProjectGenerator
from src.project_config import ProjectConfiguration


class TestTemplateGenerator(TestCase):

    def setUp(self):
        self.tmp_path = os.getcwd() + "/tmp/"
        self.conf_file = "project.yml"
        self.file_path = self.tmp_path + "/" + self.conf_file
        self.configuration = test_configuration
        self.__create_file(self.file_path)
        self.folder_structures = [
            "pyprojectgen",
            "pyprojectgen/src",
            "pyprojectgen/tests",
        ]

    def tearDown(self):
        self.__remove_file(self.file_path)
        self.__remove_dir(self.tmp_path + self.folder_structures[2])
        self.__remove_dir(self.tmp_path + self.folder_structures[1])
        self.__remove_dir(self.tmp_path + self.folder_structures[0])

    def __create_file(self, file_path):
        if not os.path.exists(self.tmp_path):
            os.mkdir(self.tmp_path)

        with open(file_path, 'w') as stream:
            content = yaml.dump(self.configuration, default_flow_style=False)
            stream.write(content)

    def __remove_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    def __remove_dir(self, dir_path):
        if os.path.exists(dir_path):
            os.rmdir(dir_path)

    def __get_path_from_structure(self, index):
        return self.tmp_path + "/" + self.folder_structures[index]

    def test_generate_project(self):
        configuration = ProjectConfiguration(self.file_path)
        generator = ProjectGenerator(configuration)
        generator.generate(self.tmp_path)
        expected = self.__get_path_from_structure(1)
        self.assertTrue(os.path.exists(expected), "Could not find ("+ expected + ")")

