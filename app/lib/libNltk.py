from nltk.tokenize import word_tokenize
from nltk import pos_tag
import textblob


class libNltk:
    @staticmethod
    def tokenize_sentence(sentence):
        if isinstance(sentence, str):
            return word_tokenize(sentence)

        return word_tokenize(sentence.decode('utf-8'))

    @staticmethod
    def pos_tagging(statement):
        tags = {
            'NN': 'Noun',
            'JJ': 'Adjective',
            'NNS': 'Plural Noun',
            'CC': 'Coordinating Conjunction',
            'CD': 'Cardinal Digit',
            'DT': 'Determiner',
            'EX': 'Existential',
            'FW': 'Foreign Word',
            'IN': 'Preposition/Subordinating Conjunction',
            'JJR': 'Comparative Adjective',
            'JJS': 'Superlative Adjective',
            'LS': 'List Marker',
            'MD': 'Modal',
            'NNP': 'Proper Noun',
            'NNPS': 'Proper Plural Noun',
            'PDT': 'Predeterminer',
            'POS': 'Possessive Ending',
            'PRP': 'Personal Pronoun',
            'PRP$': 'Possessive Pronoun',
            'RB': 'Adverb',
            'RBR': 'Comparative Adverb',
            'RBS': 'Superlative Adverb',
            'RP': 'Particle',
            'TO': 'TO',
            'UH': 'Interjection',
            'VB': 'Verb',
            'VBD': 'Past Tense Verb',
            'VBG': 'Present Participle Verb/Gerund',
            'VBN': 'Past Participle Verb',
            'VBP': 'Present Verb',
            'VBZ': 'Third Person Present Verb',
            'WDT': 'Wh-Determiner',
            'WP': 'Wh-Pronoun',
            'WP$': 'Possessive Wh-Pronoun',
            'WRB': 'Wh-Adverb'
        }
        statement = textblob.Word(statement).lemmatize()
        _, tag = pos_tag([statement])[0]
        return [statement, tags[tag]]
