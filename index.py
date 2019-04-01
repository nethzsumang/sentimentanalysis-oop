from bootstrap import bootstrap
from framework.Utilities.Packager import version_check


version_check()

import nltk


# download nltk data
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('wordnet', quiet=True)

bootstrap.start()
