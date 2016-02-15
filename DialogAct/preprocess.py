__author__ = 'rodas'

from collections import defaultdict

from nltk.stem.porter import *

from swda import CorpusReader


def preprocess():
    stemmer = PorterStemmer()
    corpus = CorpusReader('swda')
    stoplist =set([line.strip() for line in open("stopword", 'r')])
    frequency = defaultdict(int)
    #fl1 = open("before-vector.txt", "wb")
    #fl = open('corpusdict.txt','w');
    #fl = open('tag.txt','w');


    corpusDict = [[[stemmer.stem(word.translate(None, "?.,-").strip())
         for word in utt.text.lower().split() if word.translate(None, "?.,-") not in stoplist],utt.damsl_act_tag()]
         for utt in corpus.iter_utterances(display_progress=True)]
    #for key in corpusDict:
        #fl.write("%s\n" % key[1])
    #fl.close()
    texts =[]
    for i in corpusDict:
        texts.append(i[0])

    for text in texts:
       for token in text:
           frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 10]  for text in texts]
    #for vector in texts:
        #fl1.write("%s\n" % vector)
    #fl1.close()
    return texts


if __name__ == '__main__':
    preprocess()