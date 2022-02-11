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
            for i in ind[0]:
                if self.awords[i][1] != "pl":
                    return self.awords[i][1]
                    
    def dative(self,word,plural):
        theword = word.split(" ")
        the = theword[0]
        word = theword[1]
        if the[0].lower() == "d" and len(the)==3:
            if the.lower()=="die":
                if not plural:
                    the = "der"
                else:
                    the = "den"
            elif the.lower()=="der":
                the = "dem"
            elif the.lower()=="das":
                the = "dem"
            return the + " " + word
        else:
            if the[-1].lower() == "e":
                if not plural:
                    the=the+"r"
                else:
                    the=the+"n"
            else:
                gen = self.get_gender(word)
                if(gen == "n"):
                    the = the+"em"
                if(gen == "m"):
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

print(g.dative("eine frau",False))
print(g.dative("kein hund",False))
print(g.dative("ein wasser",False))
