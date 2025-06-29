import spacy
import nltk
from nltk.corpus import words

# Download NLTK resources if needed
nltk.download('words')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
nouns=['April', 'Sundar', 'Pichai', 'Google', 'AI', 'Gemini', 'Barack', 'Obama', 'Harvard', 'University', 'X', 'Veermata', 'Jijabai', 'Technological', 'Institute', 'Mumbai', 'BTech', 'Mechanical', 'Engineering', 'VJTI']

tests=["""In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini.
Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education.""", """Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together.
Through the guidance of their mcntors these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice.""", """I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028""", "However the rcsults were clear"]

def fix_error(word):
    corrections = {
            '0': 'o',
            '1': 'l',
            '5': 's',
            'e': 'c',
            'c': 'e'
        }
    corrected = word
    for wrong, right  in corrections.items():
        corrected = corrected.replace(wrong, right)
    
    return corrected

# Get set of English words from NLTK
english_vocab = set(w.lower() for w in words.words())

for text in tests:
    doc = nlp(text)

#misspelled = [token.text for token in doc if token.is_alpha and token.text.lower() not in english_vocab and token.text not in nouns]

    corrected=""
    for token in doc:
        if token.is_alpha and token.text.lower() not in english_vocab and token.text not in nouns:
            corrected = corrected + " " + fix_error(token.text)
        else:
            corrected = corrected + " " + token.text
    
    print(corrected)
