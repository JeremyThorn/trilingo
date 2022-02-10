def dative(word,plural):
    theword = word.split(" ")
    the = theword[0]
    word = theword[1]
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

print(dative("das wasser",False))
