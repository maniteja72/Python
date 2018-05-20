import random
from collections import Counter

someWords = '''kartheek kamala chilla venkat srikar siddarth manikanta'''

someWords = someWords.split('')
word = random.choice(someWords)

if _name_ == ' _main_ ':
    print(' Guess the words from the fill blanks ! The HINT is they are my family names')

    for i in word:

        print( '_', end = '')
        print()
        playing = True
        letterGuessed = ''
        chances = len(word) +2
        correct = 0

        try:

            while (chances != 0)
            print()
            chances -= 1

            try:
                guess = str(input('Enter the letter to guess the word: '))
            except:
                print('enter only a single letter!')
                continue

                if not guess.isalpha():
                    print(' enter only 1 letter')
                    continue
                elif len(guess) > 1:
                    print('enter only a single letter!')
                    continue
                elif guess in letterGuessed:
                    print(' You have already gueesed the letter')
                    continue

                    if guess in word:
                        if char in letterGuessed:
                            print(char, end = '')
                            correct += 1
                        else:
                            print('_', end = '')

                            if (Counter(leterGuessed) == Conunter(word)):
                                print()
                                print('congratulations')
                                break

                                if chance == 0:
                                    print()
                                    print('Lost')
                                    print( ' The word was {}'. format(word))

                                    if chances ==0:
                                        print()
                                        print(' bye ')
                                        exit()






