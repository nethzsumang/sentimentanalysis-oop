from app.bl.blFile import blFile
from framework.MVC.Controller import Controller


class TobaccoController(Controller):
    @staticmethod
    def check_cache(o_app, a_params):
        filename = o_app.get('APP', 'TOBACCO')['PICKLE_FILE']
        exists = blFile.checkIfExists(filename)
        if exists:
            return Controller.redirect('TobaccoController@get_cache', {})

        return Controller.redirect('TobaccoController@fetch_tweets', {})

    @staticmethod
    def fetch_tweets(o_app, a_params):
        print('Fetching tobacco tweets...')
        pass

    @staticmethod
    def get_cache(o_app, a_params):
        print('Getting tobacco tweets cache...')
        pass

    @staticmethod
    def analyze(o_app, a_params):
        pass

    @staticmethod
    def show_graph(o_app, a_params):
        print('Showing tobacco graph...')
        pass
