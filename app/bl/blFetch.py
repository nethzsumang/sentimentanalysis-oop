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
        end_month, end_year = blFetch._get_next_month(end_month, end_year)

        while not blFetch._compare_months([month, year], [end_month, end_year]):
            start_date = Date(a_date=[year, month, 1]).get("%Y-%m-%d")
            end_day = Date.get_last_day_of_month(year, month)
            end_date = Date(a_date=[year, month, end_day]).get("%Y-%m-%d")

            arr_monthly_data.append(MonthlyData(start_date, end_date))

            if month == 12:
                arr_yearly_data.append(YearlyData(arr_monthly_data))
                arr_monthly_data = []
            else:
                if blFetch._compare_months(
                    [month, year], blFetch._get_prev_month(end_month, end_year)
                ):
                    arr_yearly_data.append(YearlyData(arr_monthly_data))
                    arr_monthly_data = []

            month, year = blFetch._get_next_month(month, year)

        return arr_yearly_data

    @staticmethod
    def _get_next_month(month, year):
        month = month + 1

        if month > 12:
            year = year + 1
            month = 1

        return [month, year]

    @staticmethod
    def _get_prev_month(month, year):
        month = month - 1

        if month < 0:
            year = year - 1
            month = 12

        return [month, year]

    @staticmethod
    def _compare_months(date1, date2):
        month1, year1 = date1
        month2, year2 = date2

        if month1 == month2 and year1 == year2:
            return True

        return False
