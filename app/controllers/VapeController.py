from app.bl.blFile import blFile
from framework.MVC.Controller import Controller


class VapeController(Controller):
    @staticmethod
    def check_cache(o_app, a_params):
        filename = o_app.get('APP', 'VAPE')['PICKLE_FILE']
        exists = blFile.checkIfExists(filename)
        if exists:
            return Controller.redirect('VapeController@get_cache', {})

        return Controller.redirect('VapeController@fetch_tweets', {})

    @staticmethod
    def fetch_tweets(o_app, a_params):
        print('Fetching vape tweets...')
        pass

    @staticmethod
    def get_cache(o_app, a_params):
        print('Getting vape tweets cache...')
        pass

    @staticmethod
    def show_graph(o_app, a_params):
        print('Showing vape graph...')
        pass