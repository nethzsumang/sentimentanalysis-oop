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
