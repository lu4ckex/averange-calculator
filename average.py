print ('--------- Student Average Calculator v1.0 ---------')
print ()

#This calculator computes the student's average by taking the theoretical, practical, and assignment grades and averaging them.

notat = float(input('Enter the theoretical grade: '))
notap = float(input('Enter the practical grade: '))
notatr = float(input('Enter the assignment grade: '))
               
media = (notat + notap + notatr) / 3
print()
print ('The students average is: ', media)