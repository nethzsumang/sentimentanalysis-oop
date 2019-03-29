from app.lib.libNltk import libNltk
from app.lib.libVader import libVader


class blWordTag:
    def __init__(self):
        pass

    @staticmethod
    def remove_noise(data):
        print("Getting word tags...")
        TWEETS_TO_ANALYZE = 50
        finished_word_tags = False
        word_tags = []

        for yearly_data in data:
            for monthly_data in yearly_data.monthly_data:
                for tweet_statement in monthly_data.twitter:
                    statement = tweet_statement.message

                    # separate tokens/words
                    statement_arr = libNltk.tokenize_sentence(statement)
                    # removes neutral words
                    statement_arr = libVader.remove_noise(statement_arr)

                    tweet_statement.message = " ".join(statement_arr)

                    if not finished_word_tags:
                        if len(word_tags) >= TWEETS_TO_ANALYZE:
                            finished_word_tags = True
                            word_tags = word_tags[:TWEETS_TO_ANALYZE]
                        else:
                            word_tags = word_tags + statement_arr
        return [data, word_tags]

    @staticmethod
    def analyze_word_tags(word_tags):
        print("Analyzing word tags...")
        result_arr = []

        for tag in word_tags:
            response = libVader.analyze(tag)
            word, tag_value = libNltk.pos_tagging(tag)
            result_arr.append(
                {
                    "statement": word,
                    "pos": response["pos"],
                    "neg": response["neg"],
                    "tag": tag_value,
                }
            )

        return result_arr
