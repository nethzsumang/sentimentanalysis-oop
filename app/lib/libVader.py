from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class libVader:
    def __init__(self):
        pass

    @staticmethod
    def analyze(s_statement):
        return SentimentIntensityAnalyzer().polarity_scores(s_statement.decode("utf-8"))
