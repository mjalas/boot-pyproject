import json
import yaml


class SetupTemplateBuilder(object):
    """Template builder class."""
    @staticmethod
    def create_setup_data():
        """Creates a dictionary containing project metadata keys."""
        setup_data = {
            'metadata': {
                'NAME': '',
                'VERSION': '',
                'DESCRIPTION': '',
                'URL': '',
                'AUTHOR': '',
                'AUTHOR_EMAIL': '',
                'LICENSE': '',
                'KEYWORDS': '',
                'CLASSIFIERS': [
                    'Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Libraries',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3.5',
                ],
                'EXCLUDE': [
                    'tests'
                ],
                'SETUP_REQUIRES': [
                    'nose>=1.0',
                    'coverage>=4.0.3',
                ],
                'TEST_SUITE': 'nose.collector',
                'TESTS_REQUIRES': ['nose']
            },
            'license': {
                'name': '',
                'name_comment': 'Name options: MIT, GNU GPLv3',
                'file': '',
                'file_comment': 'File options: MIT, GPL3'
            },
            'readme': {
                'header': '',
                'description': ''
            }
        }
        return setup_data

    @staticmethod
    def build_json():
        """Creates the json version of project metadata template."""
        result = SetupTemplateBuilder.create_setup_data()
        return json.dumps(result, indent=4, separators=(',', ': '))

    @staticmethod
    def build_yaml():
        """Creates the yaml version of project metadata template."""
        result = SetupTemplateBuilder.create_setup_data()
        return yaml.dump(result, default_flow_style=False)
