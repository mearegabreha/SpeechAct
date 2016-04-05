__author__ = 'rodas'

from collections import defaultdict
from operator import itemgetter
from swda import CorpusReader
from sys import argv
from gensim import corpora, models, similarities
from nltk.stem.porter import *


def Atag():
        corpus = CorpusReader('swda')
        actTag = defaultdict(int)
        for utt in corpus.iter_utterances(display_progress=True):
            actTag[utt.damsl_act_tag()] +1
        i=1
        for key in actTag.keys():
            actTag[key] = i
            i=i+1
        print actTag
        return actTag

if __name__ == '__main__':
    Atag()