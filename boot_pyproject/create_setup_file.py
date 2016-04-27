import json


class SetupFileBuilder(object):

    @staticmethod
    def build():
        setup_data = {}
        return json.dumps(setup_data)
