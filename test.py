import re

ofile = open("nouns.txt","w")
file = open("../all.txt","r")
lines = file.readlines()
for i in lines:
    if("noun" in i):
        add = True
        new_word = ""
        for j in i:
            #print(j)

            if(j=="[" or j == "<" or j == "("):
                add = False

            if(add):
                new_word=new_word+j

            if(j == "]" or j == ">" or j == ")"):
                add = True
        #print(new_word)
        words = re.split("\t",new_word)
        gw= ""
        gen = ""
        add = True
        for j in words[0]:
            #print(j)

            if(j=="{"):
                add = False

            if(add):
                gw=gw+j
            else:
                gen = gen + j

            if(j == "}"):
                add = True
        german = gw.replace("  "," ")
        gender = gen[1:-1]
        if len(words) >=2:
            english = words[1]
        else:
            english = "N/A"
        ofile.write(german+","+gender+","+english+"\n")
file.close()
ofile.close()
