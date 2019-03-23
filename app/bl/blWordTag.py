from app.lib.libNltk import libNltk
from app.lib.libVader import libVader


class blWordTag:
    def __init__(self):
        pass

    @staticmethod
    def create_word_tags(data):
        print('Getting word tags...')
        TWEETS_TO_ANALYZE = 10
        word_tags = []

        for yearly_data in data:
            for monthly_data in yearly_data.monthly_data:
                for tweet_statement in monthly_data.twitter:
                    statement = tweet_statement.message

                    # separate tokens/words
                    statement_arr = libNltk.tokenize_sentence(statement)
                    # removes neutral words
                    statement_arr = libVader.remove_noise(statement_arr)

                    word_tags = word_tags + statement_arr

                    if len(word_tags) >= TWEETS_TO_ANALYZE:
                        word_tags = word_tags[:10]
                        return word_tags

        return word_tags

    @staticmethod
    def analyze_word_tags(word_tags):
        result_arr =[]

        for tag in word_tags:
            response = libVader.analyze(tag)
            result_arr.append({
                'statement': tag,
                'pos': response['pos'],
                'neg': response['neg'],
                'tag': libNltk.pos_tagging(tag)
            })

        return result_arr
