from unittest import TestCase
from boot_pyproject.create_setup_file import SetupTemplateBuilder
import json


class TestSetupTemplateBuilder(TestCase):

    def test_create_setup_file(self):
        expected = {}
        result = SetupTemplateBuilder.build()
        self.assertEqual(expected, json.loads(result))
