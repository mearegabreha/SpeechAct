__author__ = 'rodas'


from gensim import corpora, models, similarities
import logging
from matplotlib import pyplot
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def lsi_topic_transform():
    dictionary = corpora.Dictionary.load('/tmp/speechact.dict')
    corpus = corpora.MmCorpus('/tmp/corpus.mm')
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    fl = open("corpus/lsi-corpus-tfid.txt", "wb")
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=20)
    #lsi.print_topics(20,60)
    corpus_lsi = lsi[corpus]
    for doc in corpus_lsi:
        fl.write("%s\n" % doc)



if __name__ == '__main__':
     lsi_topic_transform()
