print "hangman game"
lives=6
word="hello"
for i in range(len(word)):
    n="_"
    print n,
l=list(n*len(word))
print "\n",l,
count=0
while(lives>0):
    guess=raw_input("\n enter the guess")
    if guess not in word:
        lives=lives-1
        print "now lives are =",lives
    for i in word:
        if(guess==i):
            print guess
            l[word.index(guess)]=guess
            print l
            count=count+1
    if count==len(word):
        print "you win"
        break
if(lives==0):
    print "you lose"


    
