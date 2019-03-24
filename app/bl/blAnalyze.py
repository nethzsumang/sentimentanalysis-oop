from app.lib.libVader import libVader


class blAnalyze:
    @staticmethod
    def analyze_tweets(a_data):
        for o_yearly_data in a_data:
            for o_monthly_data in o_yearly_data.monthly_data:
                a_twitter_statements = o_monthly_data.twitter

                for o_statement in a_twitter_statements:
                    s_statement = o_statement.message
                    a_sentiment = libVader.analyze(s_statement)
                    o_statement.set_score(a_sentiment)
                    o_statement.analyze_score()

        return a_data

    @staticmethod
    def analyze_per_month(data):
        for yearly_data in data:
            for monthly_data in yearly_data.monthly_data:
                monthly_data.analyze_month_twitter()

        for yearly_data in data:
            yearly_data.analyze_year_twitter()

        return data
