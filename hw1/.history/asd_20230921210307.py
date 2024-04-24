import numpy as np
import nltk
import re

# The first time you will need to download the corpus:

nltk.download()

pirates_txt = nltk.corpus.webtext.raw('pirates.txt')
