# Name:zeke
# Date:7/12/17
#
# """
# proj04
#
# Asks the user for a string and prints out whether or not the string is a palindrome.
#
# """
name = raw_input('Name: ')
date = raw_input('Date: ')
str = raw_input('What word would you like me to check to see if it is a palindrome:')
lst = []
for letter in str:
    lst.append(letter)
c = []
for letter in str:
    c.append(letter)
a = lst
print a
#c = lst
c.reverse()
print lst, c
#c = list
if lst == c:
    print'Congratulations you found a palindrome'
if lst != c:
    print'Sorry this is not a palindrome'
