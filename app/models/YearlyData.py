from framework.MVC.Model import Model


class YearlyData(Model):
    year = ""
    monthly_data = []

    twitter_pos_ave = 0
    twitter_neg_ave = 0
    twitter_neu_ave = 0

    def __init__(self, a_monthly_data):
        self.monthly_data = a_monthly_data
        self.year = self.monthly_data[0].year
        self.db_ref = False
        super().__init__()

    def analyze_year_twitter(self):
        i_no_of_months = len(self.monthly_data)
        pos_tot = 0.0
        neg_tot = 0.0
        neu_tot = 0.0

        for o_monthly_data in self.monthly_data:
            pos_tot += o_monthly_data.twitter_pos_per
            neg_tot += o_monthly_data.twitter_neg_per
            neu_tot += o_monthly_data.twitter_neu_per

        self.twitter_pos_ave = pos_tot / i_no_of_months
        self.twitter_neg_ave = neg_tot / i_no_of_months
        self.twitter_neu_ave = neu_tot / i_no_of_months
