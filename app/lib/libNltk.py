from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer


class libNltk:
    @staticmethod
    def tokenize_sentence(sentence):
        return word_tokenize(sentence.decode('utf-8'))

    @staticmethod
    def pos_tagging(statement):
        statement = WordNetLemmatizer().lemmatize(statement)
        _, tag = pos_tag([statement])[0]
        return tag
