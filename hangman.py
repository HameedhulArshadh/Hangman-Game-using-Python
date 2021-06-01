from random import randint
def head():
    print("===============")
    print("--------\n    |\n    😁")

def body():
    print("===============")
    print("--------\n    |\n    😰\n     |")

def hands():
    print("===============")
    print("--------\n    |\n    😱\n    /|\\")
    
def legs():
    print("===============")
    print("You Lost 😑  😑")
    print("--------\n    |\n    😵\n    /|\\\n    / \\")
    
def refresh():
    words = ["apple","orange","pineapple","papaya", "acerolo","apricot","avocado","banana","strawberry","blackberry","blackcurrant","carambola","cherimoya", "cherries", "clementine", "grapes", "kiwi"]
    value = randint(0,len(words)-1)
    word = words[value]
    return word

def display(wordlist,dispWord,key): #wordlist,dispWord,letter
    i = 0
    for letter in wordlist:
        if(letter == key):
            dispWord[i] = key
        i +=1
    return dispWord

def wins():
    print(" You've won 🥳  🥳  🥳")
    
  
lives = 4
word = refresh()
wordlist = []
for i in word:
    wordlist.append(i)


dispWord = list("_"*len(word))
win = 0
guess = set()

while lives!=0 and win ==0:
    print(dispWord)
    print()
    letter = input("Enter a letter:")
    if(letter in word):
        if(letter not in guess):
            guess.add(letter)
            print("good guess  🎉")
            dispWord = display(wordlist,dispWord,letter)
        else:
            print("You already guessed it, try other word")
    else:
        if (letter not in guess):
            lives -=1
            guess.add(letter)
            print("bad guess  🤡")
            if(lives == 3):
                head()
            elif(lives == 2):
                body()
            elif(lives ==1):
                hands()
            else:
                legs()
        else:
            print("You already guessed it, try other word")
        
    if(dispWord == wordlist):
        win = 1;
        wins()
        print(dispWord)
        
