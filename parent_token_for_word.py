import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt')
text = "inserisci frase"
doc = nlp(text)
for word in doc.sentences[0].words:
    print(f'word: {word.text}\tparent token: {word.parent.text}')