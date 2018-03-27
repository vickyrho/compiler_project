import sys
import re

from pprint import pprint

from nltk.tree import *
import gensim
from gensim import corpora
from stat_parser import Parser
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized
				
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


file = sys.argv[1]

fp = open(file,"r")
doc_complete=[]
doc_clean=[]
str = fp.read()

sentences = re.split("[.?!'\n'][\s]*",str)

parser = Parser()


for sent in sentences:
	if(len(sent)>10):
		doc_complete.append(sent)
		tokenized = custom_sent_tokenizer.tokenize(sent)
		process_content()

		

doc_clean = [clean(doc).split() for doc in doc_complete]

dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
corpus = [dictionary.doc2bow(doc) for doc in doc_clean]

# print(doc_clean)

# print(doc_term_matrix)

# Creating the object for LDA model using gensim library
LDA = gensim.models.ldamodel.LdaModel

ldamodel = LDA(corpus=corpus, num_topics=1, id2word=dictionary)

pprint(ldamodel.show_topics())





