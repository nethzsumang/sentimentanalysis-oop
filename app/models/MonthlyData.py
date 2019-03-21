from framework.MVC.Model import Model


class MonthlyData(Model):
    since = ""
    until = ""
    month_numstring = ""
    twitter = []
    facebook = []
    reddit = []
    youtube = []

    twitter_tot = 0
    twitter_pos = 0
    twitter_neg = 0
    twitter_neu = 0

    twitter_pos_per = 0.0
    twitter_neg_per = 0.0
    twitter_neu_per = 0.0

    def __init__(self, since, until):
        self.since = since
        self.until = until
        self.month_numstring = self.since[0:4] + "-" + self.since[5:7]
        self.year = self.since[0:4]
        self.month = self.since[5:7]
        self.db_ref = False
        super().__init__()

    def since_unix(self):
        s_day = self.since[8:10]

        import datetime
        import time

        o_datetime = datetime.datetime(
            int(self.year), int(self.month), int(s_day), 0, 0
        )
        return time.mktime(o_datetime.timetuple())

    def until_unix(self):
        s_year = self.until[0:4]
        s_month = self.until[5:7]
        s_day = self.until[8:10]

        import datetime
        import time

        o_datetime = datetime.datetime(int(s_year), int(s_month), int(s_day), 0, 0)
        return time.mktime(o_datetime.timetuple())

    def analyze_month_twitter(self):
        self.twitter_tot = len(self.twitter)
        self.twitter_pos = 0
        self.twitter_neg = 0
        self.twitter_neu = 0

        for o_statement in self.twitter:
            s_grade = o_statement.sentiment_grade
            if s_grade == "positive":
                self.twitter_pos += 1
            elif s_grade == "negative":
                self.twitter_neg += 1
            elif s_grade == "neutral":
                self.twitter_neu += 1
            else:
                raise Exception("Statement is not yet analyzed!")

        self.twitter_pos_per = (self.twitter_pos / self.twitter_tot) * 100
        self.twitter_neg_per = (self.twitter_neg / self.twitter_tot) * 100
        self.twitter_neu_per = (self.twitter_neu / self.twitter_tot) * 100

        return

    def get_tweet_counts(self):
        return [self.twitter_tot, self.twitter_pos, self.twitter_neu, self.twitter_neg]

    def get_tweet_percents(self):
        return [self.twitter_pos_per, self.twitter_neu_per, self.twitter_neg_per]
