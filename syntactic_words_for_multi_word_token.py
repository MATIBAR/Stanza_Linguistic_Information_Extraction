import stanza
# Commento:per frasi contenenti parole comoposte (es: "dalla")
nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt')
text = "sono andato dalla mamma"
doc = nlp(text)
for token in doc.sentences[0].tokens:
    print(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}')