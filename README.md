# SpeechAct
code used to prepare Switchboard Dialog Act corpus in the form of vector for SVM classifier

preprocess.py <br />
    + read the SWDA corpus <br />
    + uses Porter Stemmer to convert words to there stem <br />
    + stop words which found in "corpus/stopword" will be removed  <br />
    + words with frequency count less than 10 is removed <br />
dictionary.py <br />
    + prepare a dictionary using gensim library and the preprocessed data <br />
DocToBOw.py <br />
    + create a BOW corpus using the dictionary created before <br />
lsi_topic_trans.py/lda_topic_trans.py <br />
    + transform the BOW corpus to other representation using LSI/LDA <br />
postprocess.py <br />
    + append class label to the vectors <br />
final-cleanup.py <br />
    + remove unnecessary characters and prepare the final corpus for LIBSVM <br />
