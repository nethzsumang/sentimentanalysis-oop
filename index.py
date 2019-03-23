from bootstrap import bootstrap
from framework.Utilities.Packager import version_check


version_check()

import nltk


# download nltk data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

bootstrap.start()
