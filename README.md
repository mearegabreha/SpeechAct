# SpeechAct
code used to prepare Switchboard Dialog Act corpus in the form of vector for SVM classifier

preprocess <br />
    + read the SWDA corpus
    + uses Porter Stemmer to convert words to there stem
    + stop words which found in "corpus/stopword" will be removed 
    + words with frequency count less than 10 is removed 
dictionary
    prepare a dictionary using gensim library and the preprocessed data
DocToBOw
    create a BOW corpus using the dictionary created before
lsi_topic_trans/lda_topic_trans
    transform the BOW corpus to other representation using LSI/LDA
postprocess
    append class label to the vectors
final-cleanup
    remove unnecessary characters and prepare the final corpus for LIBSVM
