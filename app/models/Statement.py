from framework.MVC.Model import Model


class Statement(Model):
    origin = ""
    message = ""
    date = ""
    sentiment_score = 0
    sentiment_grade = ""
    pos = 0.0
    neg = 0.0
    neu = 0.0
    compound = 0.0
    objectivity_score = 0

    def __init__(self, a_data):
        self.origin = a_data["origin"]
        self.message = a_data["message"].encode("utf-8")
        self.date = a_data["date"]
        self.db_ref = False
        super().__init__()

    def set_score(self, a_sentiment):
        self.pos = a_sentiment["pos"]
        self.neg = a_sentiment["neg"]
        self.neu = a_sentiment["neu"]
        self.compound = a_sentiment["compound"]

    def analyze_score(self):
        if self.compound >= 0.05:
            self.sentiment_grade = "positive"
        elif self.compound <= -0.05:
            self.sentiment_grade = "negative"
        else:
            self.sentiment_grade = "neutral"
