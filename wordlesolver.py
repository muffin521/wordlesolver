import re

# get input, loop if len != 5 (aka not a valid wordle word)
green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')
while len(green) != 5:
    print("not a valid input")
    green = raw_input('what are your green letters? input \".\" if you do not have a green letter for that position\n')

# get yellow letters
yellow = raw_input('what are your yellow letters? do not enter any characters other than the letters. if none, hit enter or simply type \".\"\n')

gray = raw_input('what are the gray letters? These are the ones that cannot be in the word. If none, simply type \'.\'\n')


# starting list of all words, only filtered for green
words = []

# only words that ALSO contain yellow letters
yellowwords = []

#remove gray letters, left with only good words!
goodwords = []

###-----------MAIN-----------###
with open('valid-wordle-words.txt', 'r') as fp:
    for line in fp:
        if green == '.....':
            for line in fp:
                line.strip('[').strip(']').strip()
                line.strip()
                words.append(line)
            # wordleword = fp.readline()
            # wordleword.replace ('[', '').replace(']','')
            # words.append(wordleword)
        else:
            word = re.findall(green, line)
            if word:
                add = word[0]
                # make pretty (remove [])
                add.replace ('[', '').replace(']','')

                words.append(add)

# only add things that also match yellow letters

if yellow == '.':
    yellowwords = words
else:
    for i in words:
        for c in yellow:
            index = i.find(c)

            if index != -1:
                yellowwords.append(i)

# remove anything that matches a gray letter
if gray == '.':
    goodwords = yellowwords
else:
    for i in yellowwords:
        addword = 1
        # checks each letter in the gray list
        for c in gray:
            index = i.find(c)
             
            # if any letter in the word IS in the gray list, set to not add to word
            if index != -1:
                addword = 0

        # to add or not to add  
        if addword == 1:
            goodwords.append(i)
            # print(i)


# output
print('Possible words:')

for i in goodwords:
    # aesthetics again
    i.strip()
    print(i)
if len(goodwords) == 0:
    print('No valid words')



