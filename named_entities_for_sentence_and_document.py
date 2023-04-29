import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,ner')
text = "inserisci frase"
doc = nlp(text)
print(*[f'entity: {ent.text}\ttype: {ent.type}' for ent in doc.ents], sep='\n')