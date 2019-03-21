from framework.Data.File.File import File


class blFile:
    def __init__(self):
        pass

    @staticmethod
    def checkIfExists(filepath):
        return File.is_exists(filepath)
