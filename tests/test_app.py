from unittest import TestCase
from src.app import App


class TestApp(TestCase):

    def test_run(self):
        app = App()
        app.run()
