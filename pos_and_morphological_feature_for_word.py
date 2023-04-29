import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt,pos')
text = "inserisci frase"
doc = nlp(text)
print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')