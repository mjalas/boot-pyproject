from unittest import TestCase
from src.project_config import ProjectConfiguration
import json
import yaml
import os


class TestProjectConfiguration(TestCase):

    def setUp(self):
        self.conf_path = os.getcwd() + "/tmp/"
        self.conf_file = "project.yml"
        self.file_path = self.conf_path + "/" + self.conf_file
        self.configuration = {
            'license': {
                'file': 'MIT',
                'name': 'MIT'
            },
            'metadata': {
                'AUTHOR': 'Tester',
                'AUTHOR_EMAIL': 'test@test.com',
                'CLASSIFIERS': [
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3.5'
                ],
                'DESCRIPTION': 'Generates python project structure',
                'EXCLUDE': [
                    'tests'
                ],
                'KEYWORDS': '',
                'LICENSE': 'MIT',
                'NAME': 'pyprojectgen',
                'SETUP_REQUIRES': [
                    'nose>=1.0',
                    'coverage>=4.0.3'
                ],
                'TESTS_REQUIRES': [
                    'nose'
                ],
                'TEST_SUITE': 'nose.collector',
                'URL': 'https://github.com/Tester/test',
                'VERSION': '0.0.1'
            },
            'readme': {
                'description': 'Generate base file structure for python project required for creating a python package.',
                'header': 'Python project generator'
            }
        }
        self.__create_project_conf_file()

    def __create_project_conf_file(self):
        if not os.path.exists(self.conf_path):
            os.mkdir(self.conf_path)
        with open(self.file_path, 'w') as stream:
            content = yaml.dump(self.configuration, default_flow_style=False)
            stream.write(content)

    def __remove_project_conf_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.conf_path):
            os.rmdir(self.conf_path)

    def tearDown(self):
        self.__remove_project_conf_file()

    def test_parse_config(self):
        conf = ProjectConfiguration(self.file_path)
        self.assertTrue(conf.metadata)
        self.assertEqual("pyprojectgen", conf.metadata['NAME'])
        self.assertTrue(conf.readme)
        self.assertTrue(conf.license)

