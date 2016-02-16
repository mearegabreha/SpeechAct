__author__ = 'rodas'


from collections import defaultdict
from operator import itemgetter
from swda import CorpusReader
from sys import argv
from gensim import corpora, models, similarities
from nltk.stem.porter import *
from dictionary import dictionary
from preprocess import preprocess


texts= preprocess()
dictionary(texts)
dictionary = corpora.Dictionary.load('/tmp/speechact.dict')

class BowCorpus(object):
    def __iter__(self):
         for text in texts:
            yield dictionary.doc2bow(text)



if __name__ == '__main__':
    corpus = BowCorpus()
    corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)

