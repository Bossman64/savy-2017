# Name:Zeke
# Date:6/12/17

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21


result = 0
loop_control = True
while loop_control == True:
    b = int(raw_input('Enter a number to sum, or 0 to indicate you are finished'))
    if b == 0:
        loop_control = False
    result = result + b
print 'your result is'print result


print 'TELL ME YOUR MATH TEACHERS EMAIL SO I CAN TELL HER YOU ARE CHEATING'



#need more variables

