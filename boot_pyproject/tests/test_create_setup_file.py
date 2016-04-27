from unittest import TestCase
from boot_pyproject.create_setup_file import SetupFileBuilder
import json


class TestSetupFileBuilder(TestCase):

    def test_create_setup_file(self):
        expected = {}
        result = SetupFileBuilder.build()
        self.assertEqual(expected, json.loads(result))
