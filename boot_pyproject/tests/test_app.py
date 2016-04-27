from unittest import TestCase
from boot_pyproject.app import App


class TestApp(TestCase):

    def test_setup(self):
        app = App()

    def test_run(self):
        app = App()
        app.run()
