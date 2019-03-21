from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print("This is " + o_app.get("APP", "APP_NAME") + " app.")
        o_app.dump(o_app.get('APP', 'VAPE'))
        return Controller.redirect('IndexController@redirector', {'mode': 'VAPE'})

    @staticmethod
    def redirector(o_app, a_params):
        o_app.dump(a_params['mode'])
