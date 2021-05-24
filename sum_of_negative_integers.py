## Sum of Negative Integers
# Create a function that takes a string containing integers as well as other characters and return the sum of the negative integers only.

## Examples
# negative_sum("-12 13%14&-11") ➞ -23
# -12 + -11 = -23
# negative_sum("22 13%14&-11-22 13 12") ➞ -33
# -11 + -22 = -33

## Notes
# There is at least one negative integer.

import re

# check if character is a digit
def isDigit(c):
    if ord(c) >= 48 and ord(c) <= 57:
        return True
    return False

def negative_sum(str):
    str = str+' '
    negs = []
    for i, c in enumerate(str):
        if c == '-':
            for j in range(i+1,len(str)):
                if not isDigit(str[j]):
                    negs.append(int(str[i:j]))
                    break
    return sum(negs)

print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))