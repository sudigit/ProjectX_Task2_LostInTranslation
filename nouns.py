import spacy

nlp = spacy.load("en_core_web_sm")

tests=["""In April 2023, Sundar Pichai did announce that Google would be launehing a new AI product namcd Gemini.
Barack Obama also gave a speech at Harvard University, cmphasizing the role of technology in modern education.""", """Project X is an exclusive elub at Veermata Jijabai Technological Institute, Mumbai, mcant to 5erve as a healthy environment for 5tudents to learn from each other and grow together.
Through the guidance of their mcntors these 5tudents are able to complete daunting tasks in a relatively short time frame, gaining significant exposure and knowledge in their domain of choice.""", """I will be eompleting my BTech dcgree in Mechanical Engineering from VJTI in 2028""", "However the rcsults were clear"]


for text in tests:
    doc = nlp(text)

    Nouns=[]

    for i, token in enumerate(doc):
        
        if token.pos_=="PROPN" and i<len(doc)-1 and doc[i+1].pos_=="PROPN" :
            k=i
            insert=token.text
            while doc[k+1].pos_=="PROPN" and k<len(doc)-1:
                insert = insert + " "+ doc[k+1].text
                k+=1
            if insert not in Nouns:
                inside=False
                for n in Nouns:
                    if insert in n:
                        inside=True
                if not inside:
                    Nouns.append(insert)

        elif token.pos_=="PROPN" and i>0 and doc[i-1].pos_=="PROPN" :
            continue

        elif token.pos_=="PROPN" and i>0 and not doc[i-1].text=="." :
            insert=token.text
            if insert not in Nouns:
                Nouns.append(insert)

        if token.text.isupper() and i>0 and not doc[i-1].text=="." :
            insert=token.text
            if insert not in Nouns:
                Nouns.append(insert)
                
    print(Nouns)
    print("\n")