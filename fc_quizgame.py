#keeping score X out of 10 times
import os, random

count = 0
score = 0

file1 = open('tpyl1/words.txt', 'r')
file2 = open('tpyl1/definition.txt', 'r')

f1content = file1.readlines()
f2content = file2.readlines()

while count < 10:
    os.system('clear')

    wordnum = random.randint(0, len(f1content)-1)

    print 'Word:', f1content[wordnum], ''

    options = [random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1),
        random.randint(0, len(f2content)-1)]

    options[random.randint(0, 2)] = wordnum

    print '1 -', f2content[options[0]],
    print '2 -', f2content[options[1]],
    print '3 -', f2content[options[2]],

    answer = input('\nYour choice: ')

    if options[answer-1] == wordnum:
        raw_input('\nCorrect! Hit enter...')
        score = score + 1
    else:
        raw_input('\nWrong! Hit enter...')

    count = count + 1

print '\nYour score is:', score