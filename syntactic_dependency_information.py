import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt,pos,lemma,depparse')
text = "Il cane che accarezzano le bambine."
doc = nlp(text)
print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')