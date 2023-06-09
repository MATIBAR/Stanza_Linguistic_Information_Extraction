'''
Code for pretokenized text
'''
import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize', tokenize_pretokenized=True)
text = "inserisci frase"
doc = nlp(text)
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')