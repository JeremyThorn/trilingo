def dative(word,plural):
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


print(dative("das wasser",False))
