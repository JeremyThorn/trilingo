import numpy as np

class german:
    def __init__(self):
        file = open("nouns_all.txt","r")
        words = file.read()
        file.close()
        words = words.split("\n")
        self.awords = []
        for i in words:
            if len(i.split("\t")) == 3:
                self.awords.append(i.split("\t"))
        self.awords = np.array(self.awords)
        #print(self.awords)

    def get_gender(self,word):
        if word in self.awords[:,0]:
            ind = np.where(self.awords == word)
            pos = []
            for i in ind[0]:
                pos.append(self.awords[i][1])
            pos = list(set(pos))
            return pos

    def dative_aw(self,word):
        theword = word.split(" ")
        the = theword[0]
        word = theword[1]
        gen = self.get_gender(word)
        if the[0].lower() == "d" and len(the)==3:
            if the.lower()=="die":
                if "pl" not in gen:
                    the = "der"
                else:
                    the = "den"
            elif the.lower()=="der":
                the = "dem"
            elif the.lower()=="das":
                the = "dem"
            return the + " " + word
        else:
            if the[-2:] == "er":
                new_the = the[:-2]+"em"
                return new_the+" "+word
            if the[-2:] == "es":
                new_the = the[:-2]+"em"
                return new_the+" "+word
            if the[-1].lower() == "e":
                if "pl" not in gen:
                    the=the+"r"
                else:
                    the=the+"n"
            else:
                if("n" in gen):
                    the = the+"em"
                if("m" in gen):
                    the = the +"em"
            return the + " " + word






g = german()
print(g.get_gender("hund"))
print(g.get_gender("katze"))
print(g.get_gender("frau"))
print(g.get_gender("junge"))
print(g.get_gender("mann"))
print(g.get_gender("baum"))
print(g.get_gender("eule"))
print(g.get_gender("wien"))

print(g.dative_aw("eine frau"))
print(g.dative_aw("kein hund"))
print(g.dative_aw("ein wasser"))
print(g.dative_aw("die wasser"))
print(g.dative_aw("jeder hund"))
