from app.lib.libTwitter import libTwitter
from app.models.MonthlyData import MonthlyData
from app.models.Statement import Statement
from app.models.YearlyData import YearlyData
from framework.Utilities.Misc.Date import Date


class blFetch:
    def __init__(self):
        pass

    @staticmethod
    def fetch_tweets(a_params):
        time_frames = blFetch.build_time_frames_array(a_params)

        for o_yearly_data in time_frames:
            for o_monthly_data in o_yearly_data.monthly_data:
                print(
                    "Fetching tweets from "
                    + o_monthly_data.since
                    + " to "
                    + o_monthly_data.until
                    + "."
                )
                a_tweets = libTwitter.fetch_tweets(
                    a_params["TWITTER_MAX_TWEETS_PER_MONTH"],
                    a_params["TWITTER_SEARCH_QUERY"],
                    o_monthly_data.since,
                    o_monthly_data.until,
                )
                a_tweet_models = []
                for a_tweet in a_tweets:
                    a_tweet_models.append(Statement(a_tweet))

                o_monthly_data.twitter = a_tweet_models

        return {"result": True, "data": time_frames}

    @staticmethod
    def build_time_frames_array(a_params):
        arr_yearly_data = []
        arr_monthly_data = []
        year = int(a_params["START_YEAR"])
        month = int(a_params["START_MONTH"])
        end_year = int(a_params["END_YEAR"])
        end_month = int(a_params["END_MONTH"])

        while year != end_year or month != end_month + 1:
            start_date = Date(a_date=[year, month, 1]).get("%Y-%m-%d")
            end_day = Date.get_last_day_of_month(year, month)
            end_date = Date(a_date=[year, month, end_day]).get("%Y-%m-%d")

            arr_monthly_data.append(MonthlyData(start_date, end_date))

            if month == 12:
                arr_yearly_data.append(YearlyData(arr_monthly_data))
                arr_monthly_data = []
                year = year + 1
                month = 1
            else:
                if month == end_month:
                    arr_yearly_data.append(YearlyData(arr_monthly_data))
                month = month + 1

        return arr_yearly_data
