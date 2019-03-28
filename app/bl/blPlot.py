import matplotlib.pyplot as plt

from framework.Utilities.Misc.Utils import path_join


class blPlot:
    @staticmethod
    def prepare_values(a_data):
        yearly_values = []

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
    def plot(data, title):
        year_arr = []
        pos_arr = []
        neg_arr = []

        for yearly_data in data:
            year = yearly_data['year']
            sentiment = yearly_data['sentiment']

            year_arr.append(year)
            pos_arr.append(sentiment['pos'])
            neg_arr.append(sentiment['neg'])

        blPlot.plot_graph([year_arr, pos_arr, neg_arr, title])

    @staticmethod
    def plot_graph(args):
        year_arr, pos_arr, neg_arr, title = args
        plt.figure()
        plt.title(title)

        plt.plot(year_arr, pos_arr, '-go', label='Positive Percentage')
        plt.plot(year_arr, neg_arr, '-ro', label='Negative Percentage')
        plt.legend(loc='upper left')
        plt.savefig(path_join('resources', 'storage', title + '.pdf'))