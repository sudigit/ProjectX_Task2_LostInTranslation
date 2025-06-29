import spacy
import nltk
from nltk.corpus import words

nltk.download('words')

nlp = spacy.load("en_core_web_sm")
english_vocab = set(w.lower() for w in words.words())

#taken from nouns.py but separated the nouns with more than 1 word
nouns=['April', 'Sundar', 'Pichai', 'Google', 'AI', 'Gemini', 'Barack', 'Obama', 'Harvard', 'University', 'X', 'Veermata', 'Jijabai', 'Technological', 'Institute', 'Mumbai', 'BTech', 'Mechanical', 'Engineering', 'VJTI']

tests=["""In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini.
Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education.""", """Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together.
Through the guidance of their mcntor these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice.""", """I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028""", "However the rcsults were clear"]

#correcting letters
def fix_let(word):
    corrections = {
            'e': 'c',
            'c': 'e'
        }
    corrected=word
    for wrong, right  in corrections.items():
        if wrong in word:
            corrected = word.replace(wrong, right)
            #print(corrected)
    return corrected

#correcting numbers
def fix_num(word):
    corrections = {
            '0': 'o',
            '1': 'l',
            '5': 's',
        }
    corrected=word
    for wrong, right  in corrections.items():
        if wrong in word:
            corrected = word.replace(wrong, right)
            #print(corrected)
    return corrected

def isdig(word):
    for char in word:
        if char.isdigit():
            return True
        else:
            return False


for text in tests:
    doc = nlp(text)

    corrected=""
    
    for token in doc:
        if token.is_alpha and token.text.lower() not in english_vocab and token.text not in nouns:  #does not identify words with numbers
            print(token)
            corrected = corrected + " " + fix_let(token.text)
        elif not token.is_alpha:
            if not token.text.isdigit():
                print(token)
                corrected = corrected + " " + fix_num(token.text)
            else:
                corrected = corrected + " " + token.text
        else:
            corrected = corrected + " " + token.text
    
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
    