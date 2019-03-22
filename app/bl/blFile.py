import os
import xlwt

from framework.Data.File.File import File
from framework.Data.File.PickleFile import PickleFile
from framework.Utilities.Misc.Utils import path_join


class blFile:
    def __init__(self):
        pass

    @staticmethod
    def check_if_exists(filepath):
        return File.is_exists(filepath)

    @staticmethod
    def save_object(s_filename, a_data):
        try:
            pickle = PickleFile(path_join('resources', 'storage', s_filename + '.data'), 'w')
            pickle.write(a_data)
            return True
        except Exception:
            return {
                'result': False,
                'code': 'EXCEPTION_OCCURRED',
                'message': 'Saving object to pickle file failed.'
            }

    @staticmethod
    def load_object(path):
        try:
            data = PickleFile(path).read()
            return {
                'result': True,
                'data': data
            }
        except Exception:
            return {
                'result': False,
                'code': 'EXCEPTION_OCCURRED',
                'message': 'Loading pickle file failed.'
            }


    @staticmethod
    def save_to_xlsx(a_data, s_path):
        book = xlwt.Workbook()

        for o_yearly_data in a_data:
            s_year = o_yearly_data.year

            for o_monthly_data in o_yearly_data.monthly_data:
                [
                    twitter_tot,
                    twitter_pos,
                    twitter_neu,
                    twitter_neg,
                ] = o_monthly_data.get_tweet_counts()
                [
                    twitter_pos_per,
                    twitter_neu_per,
                    twitter_neg_per,
                ] = o_monthly_data.get_tweet_percents()
                month_name = calendar.month_name[int(o_monthly_data.month)]

                sheet = book.add_sheet(month_name + " " + s_year)

                sheet.write(0, 0, "Summary")
                sheet.write(2, 0, "Year")
                sheet.write(2, 1, s_year)
                sheet.write(3, 0, "Month")
                sheet.write(3, 1, month_name)
                sheet.write(4, 0, "Number of Items")
                sheet.write(4, 1, str(twitter_tot))

                sheet.write(6, 0, "Results")
                sheet.write(7, 1, "Number of Items")
                sheet.write(7, 2, "Percentage")

                sheet.write(8, 0, "Positive")
                sheet.write(8, 1, str(twitter_pos))
                sheet.write(8, 2, str(twitter_pos_per))

                sheet.write(9, 0, "Negative")
                sheet.write(9, 1, str(twitter_neg))
                sheet.write(9, 2, str(twitter_neg_per))

                sheet.write(10, 0, "Neutral")
                sheet.write(10, 1, str(twitter_neu))
                sheet.write(10, 2, str(twitter_neu_per))

                sheet.write(12, 0, "Tweets")
                sheet.write(13, 0, "Date Posted")
                sheet.write(13, 1, "Tweet")
                sheet.write(13, 2, "Polarity")
                # sheet.write(13, 3, 'Objectivity')
                sheet.write(13, 3, "Remarks")

                row_num = 14

                for o_statement in o_monthly_data.twitter:
                    sheet.write(row_num, 0, o_statement.date)
                    sheet.write(row_num, 1, o_statement.message.decode("utf-8"))
                    sheet.write(row_num, 2, o_statement.compound)
                    # sheet.write(row_num, 3, o_statement.objectivity_score)
                    sheet.write(row_num, 3, o_statement.sentiment_grade)

                    row_num = row_num + 1

        if os.path.isfile(s_path):
            os.remove(s_path)

        book.save(s_path)