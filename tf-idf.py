import collections
import numpy as np

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/len(text)
    return tf_text


def compute_idf(word, corpus):
    return np.log(len(corpus) / sum([1.0 for i in corpus if word in i]))

documents_list = []
def compute_tfidf(corpus):
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)

    for word in computed_tf:
        tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)

    return documents_list
