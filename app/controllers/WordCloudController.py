from app.bl.blWordCloud import blWordCloud
from framework.MVC.Controller import Controller


class WordCloudController(Controller):
    @staticmethod
    def generate_word_cloud(o_app, a_params):
        blWordCloud.generate_word_cloud()
