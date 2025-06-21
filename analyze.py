import os

#function for syntax error
def getrisk(filepath):
    count = 0
    forb = False
    risk = ""

    with open(filepath, 'r') as file:
        for line in file:

            #---line length---
            if line=="\n":
                #print("new")
                continue
            
            #print(len(line))
            if line.endswith('\n'):
                checkline=line[:-1]
            else:
                checkline=line
            
            while checkline.endswith(" "):
                checkline=checkline[:-1]
            #print(len(checkline))

            if len(checkline) > 80:
                count += 1


            #---remove comment---
            x = line.split("#")[0]

            #---check forbidden keywords---
            if "print(" in x:
                forb = True
                count += 1
            if "eval(" in x:
                forb = True
                count += 1
            if "exec(" in x:
                forb = True
                count += 1

            #---check odd no of double quotes---
            if x.count('"') % 2 != 0:
                count += 1

            #---check odd no of single quotes---
            if x.count("'") % 2 != 0:
                count += 1

    # risk
    if count > 5 or forb:
        risk = "HIGH"
    elif 0 < count <= 5 and not forb:
        risk = "LOW"
    else:
        risk = "CLEAN"

    print(f"{filepath}: {risk}")




#get directory and the src folder
dir = os.path.dirname(__file__)
folder = os.path.join(dir, 'src')


#go through files in folder
for filename in os.listdir(folder):
    file = os.path.join(folder, filename)
    getrisk(file)
        