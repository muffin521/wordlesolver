import re

words = []

# get input, loop if len != 5 (aka not a valid wordle word)
green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')
while len(green) != 5:
    print("not a valid input")
    green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')

# get yellow letters
yellow = raw_input('what are your yellow letters? do not enter any characters other than the letters. if none, hit enter or simply type \".\"\n')

gray = raw_input('what are the gray letters? These are the ones that cannot be in the word. If none, simply type \'.\'\n')

# find all strings that match input
with open('valid-wordle-words.txt', 'r') as fp:
    for line in fp:
        word = re.findall(green, line)
        if word:
            add = word[0]
            # make pretty (remove [])
            add.replace ('[', '').replace(']','')

            words.append(add)

# only add things that also match yellow letters
yellowwords = []

if yellow == '.':
    yellowwords = words
else:
    for i in words:
        for c in yellow:
            index = i.find(c)

            if index != -1:
                yellowwords.append(i)

# remove anything that matches a gray letter
goodwords = []

if gray == '.':
    goodwords = yellowwords
else:
    for i in yellowwords:
        for c in gray:
            index = i.find(c)
            
            if index == -1:
                goodwords.append(i)


# output
print('Possible words:')

for i in goodwords:
    # aesthetics again
    i.strip()
    print(i)
if len(goodwords) == 0:
    print('No valid words')



