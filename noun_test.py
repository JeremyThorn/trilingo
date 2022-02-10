import random
import os
import termcolor


test = open("German.txt","r")
words = test.read()
words = words.split("\n")
words = [i.split(",") for i in words][:-1]
test.close()

test = open("Encouragement.txt","r")
enc = test.read()
enc = enc.split("\n")[:-1]
test.close()

test = open("Wrong.txt","r")
wrg = test.read()
wrg = wrg.split("\n")[:-1]
test.close()

nums = [i for i in range(len(words))]

random.shuffle(nums)


c = 0
ger = 0
running = True
max_num = 100
while running:
    ind = nums[c]
    ger = random.randint(0,1)
    print(words[ind][ger%2])
    ans =  input("")
    if ans.lower() == words[ind][(ger+1)%2].lower():
        print(termcolor.colored("Correct!\n","green"))
        anger = random.randint(0,3)
        if(anger == 0):
            print(termcolor.colored(enc[random.randint(0,len(enc)-1)]+"\n","green"))
    else:
        print(termcolor.colored("Wrong!","red"))
        print(termcolor.colored("Correct anwser: "+words[ind][(ger+1)%2]+"\n","red"))
        anger = random.randint(0,3)
        if(anger == 0):
            print(termcolor.colored(wrg[random.randint(0,len(wrg)-1)]+"\n","red"))



    c = c+1
    if(c==len(words) or c>max_num):
        running = False
