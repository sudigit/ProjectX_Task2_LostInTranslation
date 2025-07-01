import spacy
import nltk
from nltk.corpus import words

nltk.download('words')

nlp = spacy.load("en_core_web_sm")

english_vocab = set(w.lower() for w in words.words())

tests=["""In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini.
Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education.""", """Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together.
Through the guidance of their mcntor these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice.""", """I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028""", "However the rcsults were clear"]

#correcting words
def fix_er(word):
    corrections = {
        'e': 'c',
        'c': 'e',
        '0': 'o',
        '1': 'l',
        '5': 's',
    }
    corrected = ""
    cor = False

    for char in word:
        if not cor and char in corrections:
            corrected += corrections[char]
            cor = True
        else:
            corrected += char

    #print(corrected)
    return corrected


for text in tests:
    doc = nlp(text)

    corrected=""
    
    for token in doc:
        if token.text.lower() not in english_vocab and not token.text.isdigit() and not token.text[0].isupper(): 
            #print(token)
            corrected = corrected + fix_er(token.text) + " "
        else:
            corrected = corrected + token.text + " "
    
    #print(corrected)

    doc1=nlp(corrected)
    correct=""
    for i, token1 in enumerate(doc1):
        if token1.text=="However" and not doc1[i+1].text==",":
            word=token1.text + "," +" "
        else:
            word=token1.text + " "

        correct+=word
    
    print(correct)
    