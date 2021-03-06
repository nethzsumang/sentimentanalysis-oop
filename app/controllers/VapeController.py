from app.bl.blAnalyze import blAnalyze
from app.bl.blFetch import blFetch
from app.bl.blFile import blFile
from app.bl.blPlot import blPlot
from app.bl.blWordTag import blWordTag
from framework.MVC.Controller import Controller
from framework.Utilities.Misc.Utils import path_join


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
        data, word_tags = blWordTag.remove_noise(data)
        response = blWordTag.analyze_word_tags(word_tags)
        data = blAnalyze.analyze_tweets(data)
        return Controller.redirect(
            "VapeController@save_data",
            {"data": data, "cached": a_params["cached"], "word_tags": response},
        )

    @staticmethod
    def save_data(o_app, a_params):
        data = a_params["data"]
        data = blAnalyze.analyze_per_month(data)
        blFile.save_word_tags_to_xls(
            a_params["word_tags"], path_join("resources", "storage", "WordTagsVape.xls")
        )
        blFile.save_to_xlsx(data, path_join("resources", "storage", "VapeAnalysis.xls"))

        if not a_params["cached"]:
            blFile.save_object("data_vape", data)

        return Controller.redirect("VapeController@show_graph", {"data": data})

    @staticmethod
    def show_graph(o_app, a_params):
        print("Showing vape graph...")
        data = a_params["data"]
        data = blPlot.prepare_values(data)
        blPlot.plot(data, "Vape Analysis")
        return Controller.redirect("IndexController@redirector", {"mode": "TOBACCO"})
