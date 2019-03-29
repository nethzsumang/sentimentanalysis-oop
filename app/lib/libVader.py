from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class libVader:
    def __init__(self):
        pass

    @staticmethod
    def analyze(s_statement):
        if isinstance(s_statement, str):
            return SentimentIntensityAnalyzer().polarity_scores(s_statement)
        else:
            return SentimentIntensityAnalyzer().polarity_scores(
                s_statement.decode("utf-8")
            )

    @staticmethod
    def remove_noise(statement_arr):
        word_list = []
        for statement in statement_arr:
            statement = statement.lower()
            result = libVader.analyze(statement)
            pos = result["pos"]
            neg = result["neg"]

            if (neg != 0.0 or pos != 0.0) and statement not in word_list:
                word_list.append(statement)

        return list(set(word_list))
