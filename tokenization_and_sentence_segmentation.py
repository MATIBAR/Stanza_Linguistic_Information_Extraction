'''
Performing tokenization and sentence segmentation for Italian texts
'''
import stanza

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt')
text = "ciao sono mati"
doc = nlp(text)
for i, sentence in enumerate(doc.sentences):
    print(f'====== Sentence {i+1} tokens =======')
    print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')


