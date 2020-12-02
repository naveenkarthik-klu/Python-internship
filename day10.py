# 1. Write a Python program for all the cases which
# can check a string contains only a certain set
# of characters (in this case a-z, A-Z and 0-9)

import re


def re_fun(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


print(re_fun("ABCDEFabcdef123450"))
print(re_fun("*&%@#!}{"))

# 2. Write a Python program that matches a word containing 'ab'


def ab_match(text):
    patterns = 'ab'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')


print()
# 3. Write a Python program to check for a number
# at the end of a word/sentence


def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return 'Yes!Number is present at the end of string'
    else:
        return 'No!Number is not present at the end of string'


print(end_num('Naveen1207'))
print(end_num('Karthik'))

print()
print(ab_match("ac"))
print(ab_match("abc"))
print(ab_match("abbc"))


print()

# 4. Write a Python program to search the numbers (0-9)
# of length between 1 to 3 in a given string

results = re.finditer(r"([0-9]{1,3})", "123 456 789")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

print()

# 5. Write a Python program to match a
# string that contains only uppercase letters
print(bool(re.match('^[A-Z]+$', '123aAbc')))
print(bool(re.match('^[A-Z]+$', 'ABC')))
