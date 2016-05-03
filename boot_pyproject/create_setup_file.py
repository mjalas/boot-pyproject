import json
import yaml


class SetupTemplateBuilder(object):

    @staticmethod
    def create_setup_data():
        setup_data = {
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
            }
        }
        return setup_data

    @staticmethod
    def build_json():
        result = SetupTemplateBuilder.create_setup_data()
        return json.dumps(result)

    @staticmethod
    def build_yaml():
        result = SetupTemplateBuilder.create_setup_data()
        return yaml.dump(result)