from app.bl.blAnalyze import blAnalyze
from app.bl.blFetch import blFetch
from app.bl.blFile import blFile
from app.bl.blWordTag import blWordTag
from framework.MVC.Controller import Controller


class VapeController(Controller):
    @staticmethod
    def check_cache(o_app, a_params):
        filename = o_app.get("APP", "VAPE")["PICKLE_FILE"]
        exists = blFile.check_if_exists(filename)
        if exists:
            return Controller.redirect("VapeController@get_cache", {})

        return Controller.redirect("VapeController@fetch_tweets", {})

    @staticmethod
    def fetch_tweets(o_app, a_params):
        print("Fetching vape tweets...")
        data = blFetch.fetch_tweets(o_app.get("APP", "VAPE"))
        if not data["result"]:
            return Controller.error(600, "Fetching tweets failed!")

        return Controller.redirect(
            "VapeController@analyze", {"data": data["data"], "cached": False}
        )

    @staticmethod
    def get_cache(o_app, a_params):
        print("Getting vape tweets cache...")
        data = blFile.load_object(o_app.get("APP", "VAPE")["PICKLE_FILE"])
        if not data["result"]:
            return Controller.error(601, data["message"])

        return Controller.redirect(
            "VapeController@analyze", {"data": data["data"], "cached": True}
        )

    @staticmethod
    def analyze(o_app, a_params):
        data = a_params["data"]
        word_tag_arr = blWordTag.create_word_tags(data)
        response = blWordTag.analyze_word_tags(word_tag_arr)
        data = blAnalyze.analyze_tweets(data)
        return Controller.redirect(
            "VapeController@save_data", {
                "data": data,
                "cached": a_params["cached"],
                "word_tags": response
            }
        )

    @staticmethod
    def save_data(o_app, a_params):
        data = a_params["data"]
        blFile.save_vape_word_tags_to_xlsx(a_params['word_tags'])

        if not a_params["cached"]:
            blFile.save_object("data_vape", data)

        return Controller.redirect("VapeController@show_graph", {"data": data})

    @staticmethod
    def show_graph(o_app, a_params):
        print("Showing vape graph...")
        data = a_params['data']
        o_app.dump(data)
        return Controller.redirect("TobaccoController@check_cache", {})
