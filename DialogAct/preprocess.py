__author__ = 'rodas'

from collections import defaultdict
from nltk.stem.porter import *
from swda import CorpusReader


def preprocess():
    stemmer = PorterStemmer()
    corpus = CorpusReader('swda')
    stoplist =set([line.strip() for line in open("corpus/stopword", 'r')])
    frequency = defaultdict(int)
    corpusDict = [[[stemmer.stem(word.translate(None, "?.,-").strip())
         for word in utt.text.lower().split() if word.translate(None, "?.,-") not in stoplist],utt.damsl_act_tag()]
         for utt in corpus.iter_utterances(display_progress=True)]
    texts =[]
    for i in corpusDict:
        texts.append(i[0])

    for text in texts:
       for token in text:
           frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 10]  for text in texts]
    return texts


