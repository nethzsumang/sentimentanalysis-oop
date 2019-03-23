import matplotlib.pyplot as plt


class blPlot:
    @staticmethod
    def prepare_values(a_data):
        yearly_values = []

        for yearly_data in a_data:
            for monthly_data in yearly_data.monthly_data:
                monthly_data.analyze_month_twitter()

        for yearly_data in a_data:
            yearly_data.analyze_year_twitter()
            yearly_values.append({
                'year': yearly_data.year,
                'sentiment': {
                    'pos': yearly_data.twitter_pos_ave,
                    'neg': yearly_data.twitter_neg_ave,
                    'neu': yearly_data.twitter_neu_ave
                },
                'data': yearly_data
            })

        return yearly_values

    @staticmethod
    def plot_vape(data):
        year_arr = []
        pos_arr = []
        neg_arr = []

        for yearly_data in data:
            year = yearly_data['year']
            sentiment = yearly_data['sentiment']

            year_arr.append(year)
            pos_arr.append(sentiment['pos'])
            neg_arr.append(sentiment['neg'])

        # GRAPH
        plt.title('VAPE ANALYSIS')
        plt.ion()
        plt.show()

        plt.plot(year_arr, pos_arr)
        plt.plot(year_arr, neg_arr)
        plt.draw()
        plt.pause(0.001)

    @staticmethod
    def plot_tobacco(data):
        year_arr = []
        pos_arr = []
        neg_arr = []

        for yearly_data in data:
            year = yearly_data['year']
            sentiment = yearly_data['sentiment']

            year_arr.append(year)
            pos_arr.append(sentiment['pos'])
            neg_arr.append(sentiment['neg'])

        # GRAPH
        plt.figure()
        plt.title('TOBACCO ANALYSIS')
        plt.ion()
        plt.show()

        plt.plot(year_arr, pos_arr)
        plt.plot(year_arr, neg_arr)
        plt.draw()
        plt.pause(0.001)

