#This can be used to list the problems yet unsolved in C or Python
#It also lists all of the codechef problems solved alongwith number of problems
#solved in C and Python'''

#File structure is like
#C\codechef\easy
#C\codechef\medium
#C\codechef\hard
#Here C can be replaced by python or any other in the list 'top'

import glob
import os

cur = os.getcwd()
#Use Indexing according to i
top = ['c', 'python2']
extensions = ['*.c', '*.py']
#Use Indexing according to j
down = ['easy', 'medium', 'hard']

write_file = cur + '\\__codechef_status.py'
w = open(write_file, 'w+')

for j in range(len(down)):
    all_solved = set()

    #Use Indexing according to i
    solved = [0] * len(top)

    for i in range(len(top)):
        #The file structure being used is present in a folder
        #git_repo
        #Change the below file structure to go to correct directory
        os.chdir(cur + '\\..\\..\\' +
                 top[i] + '\\codechef\\' + down[j])

        temp = extensions[i]

        solved[i] = set(
            [cur_file[:len(cur_file) - len(temp) + 1].lower()
             for cur_file in glob.glob(temp)]
        )
        all_solved.update(solved[i])

    w.write("Total number of codechef " + down[j])
    w.write(" problems solved = " + str(len(all_solved)))

    if len(all_solved) > 0:
        w.write('\n\n')
        for i in range(len(top)):
            temp = all_solved - solved[i]
            w.write("\nProblems unsolved in ")
            w.write(top[i] + " = " + str(len(temp)))
            w.write("\n\n")
            for k in temp:
                w.write("#" + str(k) + "\n")

    w.write("\n----------------------------------------\n")

w.close()
