from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print("This is " + o_app.get("APP", "APP_NAME") + " app.")
        o_app.dump(o_app.get('APP', 'VAPE'))
        return Controller.redirect('IndexController@redirector', {'mode': 'VAPE'})

    @staticmethod
    def redirector(o_app, a_params):
        if a_params['mode'] == 'VAPE':
            return Controller.redirect('VapeController@check_cache', {})
        elif a_params['mode'] == 'TOBACCO':
            return Controller.redirect('TobaccoController@check_cache', {})

        return Controller.redirect(False)
