import re

words = []

green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')
while len(green) != 5:
    print("not a valid input")
    green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')

yellow = raw_input('what are your yellow letters? do not enter any characters other than the letters. if none, hit enter or simply type \".\"\n')



with open('valid-wordle-words.txt', 'r') as fp:
    for line in fp:
        word = re.findall(green, line)
        if word:
            add = word[0]
            add.replace ('[', '').replace(']','')

            words.append(add)

goodwords = []

if yellow != '.':
    for i in words:
        for c in yellow:
            index = i.find(c)

            if index != -1:
                goodwords.append(i)


print('Possible words:')

for i in goodwords:
    i.strip()
    print(i)
if len(goodwords) == 0:
    print('No valid words')



