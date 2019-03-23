from bootstrap import bootstrap
from framework.Utilities.Packager import version_check


version_check()

import nltk


# download nltk data
nltk.download('punkt')

bootstrap.start()
