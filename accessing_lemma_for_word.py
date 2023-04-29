'''
Accessing the base word form and its inflections using Stanza for Italian
'''

import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt,pos,lemma')
text = "inserisci frase"
doc = nlp(text)
print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')