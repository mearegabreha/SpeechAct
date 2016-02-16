__author__ = 'rodas'


from gensim import corpora, models, similarities
import logging
from matplotlib import pyplot
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def lda_topic_transform():
    dictionary = corpora.Dictionary.load('/tmp/speechact.dict')
    corpus = corpora.MmCorpus('/tmp/corpus.mm')
    fl = open("corpus/lda-corpus.txt", "wb")
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=20)

    #lda.print_topics(2)

    corpus_lda = lda[corpus]
    #corpora.MmCorpus.serialize('/tmp/corpuslsi.mm', corpus_lsi)


    for doc in corpus_lda:
        fl.write("%s\n" % doc)

if __name__ == '__main__':
     lda_topic_transform()