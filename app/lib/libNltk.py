from nltk.tokenize import word_tokenize


class libNltk:
    @staticmethod
    def tokenize_sentence(sentence):
        return word_tokenize(sentence.decode('utf-8'))
