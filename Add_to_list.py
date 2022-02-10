test = open("German.txt","a")

running = True
while running:
    go = input("[German],[English]:")
    if(go == "exit"):
        test.close()
        running = False
    else:
        test.write(go+"\n")
