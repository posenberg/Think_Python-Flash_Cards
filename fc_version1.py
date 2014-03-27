#keeping score X out of 10 times
import os, random, sys

a_file= open('tpyl1/words.txt', 'r')
another_file = open('tpyl1/definition.txt', 'r')

word = a_file.readlines()
definition = another_file.readlines()



    
def find_word():
    x = True
    y = 1
    while x == True:

        wordnum = random.randint(0, len(definition)-1)

        print 'What is %s' % definition[wordnum].lower()


        ans = raw_input('>')

        if ans == 'hints':
            print '\n\nSelect one of the three bitches below:'
            options = [random.randint(0, len(word)-1),
            random.randint(0, len(word)-1),
            random.randint(0, len(word)-1)]
            options[random.randint(0, 2)] = wordnum
            print '1 -', word[options[0]],
            print '2 -', word[options[1]],
            print '3 -', word[options[2]],

            second_ans_hints = raw_input('Which choice > ')
            second_ans_hints = int(second_ans_hints)-1

            if word[options[second_ans_hints]] == word[wordnum]:
                print "Correct. The answer is ", word[wordnum]

            else:
                print "Wrong. The answer is ", word[wordnum]


        else:
            print 'Answer: ', word[wordnum], ''



def find_def():
    x = True
    while x == True:

        wordnum = random.randint(0, len(word)-1)

        print 'Define %s.' % word[wordnum].lower()

        ans = raw_input('> ')

        if ans == 'hints':
            print '\n\nSelect one of the three bitches below:'
            options = [random.randint(0, len(definition)-1),
            random.randint(0, len(definition)-1),
            random.randint(0, len(definition)-1)]
            options[random.randint(0, 2)] = wordnum
            print '1 -', definition[options[0]],
            print '2 -', definition[options[1]],
            print '3 -', definition[options[2]],

            second_ans_hints = raw_input('Which choice > ')
            second_ans_hints = int(second_ans_hints)-1

            if definition[options[second_ans_hints]] == definition[wordnum]:
                print "Correct. The answer is ", definition[wordnum]

            else:
                print "Wrong. The answer is ", definition[wordnum]

        else:
            print 'Answer: ', definition[wordnum], ''

if len(sys.argv) == 2 and sys.argv[1] == "word":
    find_word()
elif len(sys.argv) == 2 and sys.argv[1] == "word": 
    find_definition()
else:
    find_definition

