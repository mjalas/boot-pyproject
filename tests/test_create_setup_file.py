from unittest import TestCase
from src.create_setup_file import SetupTemplateBuilder
import json
import yaml


class TestSetupTemplateBuilder(TestCase):

    def setUp(self):
        self.expected_dict = {
            "metadata": {
                "NAME": "",
                "VERSION": "",
                "DESCRIPTION": "",
                "URL": "",
                "AUTHOR": "",
                "AUTHOR_EMAIL": "",
                "LICENSE": "",
                "KEYWORDS": "",
                "CLASSIFIERS": [],
                "EXCLUDE": [],
                "SETUP_REQUIRES": [],
                "TEST_SUITE": "nose.collector",
                "TESTS_REQUIRES": ["nose"],
                "INSTALL_REQUIRES": []
            },
            "license": {
                "name": "",
                "name_comment": "Name options: MIT, GNU GPLv3",
                "file": "",
                "file_comment": "File options: MIT, GPL3"
            },
            "readme": {
                "header": "",
                "description": ""
            }
        }

    def test_create_setup_data(self):
        result = SetupTemplateBuilder.create_setup_data()
        self.assertEqual(self.expected_dict, result)

    def test_create_setup_json(self):
        result = SetupTemplateBuilder.build_json()
        self.assertEqual(json.dumps(self.expected_dict), result)

    def test_create_setup_yaml(self):
        result = SetupTemplateBuilder.build_yaml()
        self.assertEqual(yaml.dump(self.expected_dict), result)
