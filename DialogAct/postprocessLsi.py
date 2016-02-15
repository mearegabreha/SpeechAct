__author__ = 'rodas'

from gensim import corpora, models, similarities
from lsiTosvm  import  Atag
import fileinput

def postprocess():
    #lsi_corpus = corpora.MmCorpus('/tmp/corpuslsi.mm')
    tag_dic = Atag()
    tagid =[]
    for line in open("tag.txt", 'r'):
        tagid.append(tag_dic[line.strip()])

    i=0
   # with open('lsi-corpus.txt', 'r') as f:
    with open('lda-corpus.txt', 'r') as f:
        lines = f.readlines()
    #lines = ['1 '+line for line in lines]
    #with open('lsi-corpus.txt', 'w') as f:
        #f.writelines(lines)
    #f = open("lsi-corpus.txt", "wb")
    f = open("lda-corpus.txt", "wb")
    for line in lines:
        f.writelines([str(tagid[i])+line])
        i=i+1







if __name__ == '__main__':
     postprocess()