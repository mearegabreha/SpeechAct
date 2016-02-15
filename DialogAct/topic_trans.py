__author__ = 'rodas'

from gensim import corpora, models, similarities
import logging
from matplotlib import pyplot
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def topic_transform():
    dictionary = corpora.Dictionary.load('/tmp/speechact.dict')
    corpus = corpora.MmCorpus('/tmp/corpus.mm')
    fl = open("lsi-corpus.txt", "wb")
    #fl = open("lda-corpus.txt", "wb")
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=20)
    #lda = models.LdaModel(corpus, id2word=dictionary, num_topics=20)
    lsi.print_topics(20,60)
    #lda.print_topics(2)
    corpus_lsi = lsi[corpus]
    #corpus_lda = lda[corpus]
    #corpora.MmCorpus.serialize('/tmp/corpuslsi.mm', corpus_lsi)

    #for doc in corpus_lsi:
    #for doc in corpus_lda:
        #fl.write("%s\n" % doc)




if __name__ == '__main__':
     topic_transform()