__author__ = 'rodas'


from gensim import corpora, models, similarities




def dictionary(texts):

    dictionary = corpora.Dictionary(texts)
    dictionary.save('/tmp/speechact.dict')


