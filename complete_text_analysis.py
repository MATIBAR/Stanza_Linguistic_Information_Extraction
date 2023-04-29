'''
Complete Italian texts analysis, performing sentence segmentation, tokenization (for both single and multi-word tokens), 
extractiong POS and morphological features and syntactic dependencies informations
'''
import stanza

import sys
sys.stdout = open("C:/Users/Dell/Desktop/doc_results.txt", "w")

nlp = stanza.Pipeline(lang='it', processors='tokenize,mwt,pos,lemma,depparse') # pip install --upgrade stanza==1.2.3
counter = 0

with open("C:/Users/Dell/Desktop/doc.txt",'rt', encoding='utf-8') as file:
    for line in file:
        counter += 1
        print("\nSENTENCE NUMBER "+str(counter)+":\n"+line+"\n")

        text = line.strip()
        doc = nlp(text)

        print("tokenization and sentence segmentation\n")
        for i, sentence in enumerate(doc.sentences):
            print(f'====== Sentence {i+1} tokens =======')
            print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')

        print("\nmulti-word token\n")
        for token in doc.sentences[0].tokens:
            print(f'token: {token.text}\twords: {", ".join([word.text for word in token.words])}')

        print("\nparent token for word\n")
        for word in doc.sentences[0].words:
            print(f'word: {word.text}\tparent token: {word.parent.text}')

        print("\nPOS and morphological feature\n")
        for sent in doc.sentences:
            for word in sent.words:
                print(
                    [
                        f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}'
                        f'\tfeats: {word.feats if word.feats else "_"}'
                    ],
                    sep='\n'
                )

        print("\nlemma for word\n")
        for sent in doc.sentences:
            for word in sent.words:
                print(*[f'word: {word.text+" "}\tlemma: {word.lemma}'], sep='\n')

        print("\nsyntactic dependency info\n")
        for sent in doc.sentences:
            for word in sent.words:
                print(
                    [
                        f'id: {word.id}\tword: {word.text}\thead id: {word.head}'
                        f'\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}', 
                    ],
                    sep='\n'
                )

sys.stdout.close()
