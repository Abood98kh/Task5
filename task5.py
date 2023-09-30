# Question 1:
name = input('Please Enter Your Name ')
age = int(input('Please Enter Your Age '))
street = input('Please Enter Your Street ')
city = input('Please Enter Your City ')
country = input('Please Enter Your Country ')
# Question 2:
name = name.title()
address = f'{street.title()}, {city.title()}, {country.title()}'
print(f'"Name: {name.title()}"')
print(f'"Age: {age}"')
print(f'"Address: {address}"')
# Question 3:
print('"Hello {%s} Your age is %d Years Old, Your Address is %s."' % (name,age - 5, address))
# Question 4:
print(type(name))
print(type(str(age))) # here I followed the results shown under question 4 in the task,
# if you would like me to print the type as integer it will be : print(type(age))
print(type(street))
print(type(city))
print(type(country))
# Question 5:
print(f'"Hello {name}, How Are You? \ """ Your Age Is "{age -5}"" + And Your Country Is: {country.title()}')
# Question 6:
print(f'"Hello {name}, How Are You? \ \n""" Your Age Is "{age -5}"" + And\n Your City Is: {city.title()}')
# Question 7:
new_name = 'ITF Gsg Python'
print('First Letter Is "' + new_name[0] + '"')
print('Third Letter Is "' + new_name[2] + '"')
print('Last Letter Is "' + new_name[-1] + '"')
# Question 8:
print(new_name[-3:])
print(new_name[:3])
print(new_name[:7:2])
print(new_name[:-7:-1])
# Question 9:
strip_name = "$&$&Mohammed$&$&"
print(strip_name.strip('$&'))
# Question 10:
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'Love'))
# Questions 11 & 12:
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
# Question 13:
# Title makes the first letter of each word uppercase and the rest of the word lowercase.
# Capitalize makes only the first letter of the sentence uppercase and the rest become lowercase.
example = "i love gSG and mr. zakaria"
print(example.title())
print(example.capitalize())
# Question 14:
first_name = 'Abdalrahman'
print('***********' + first_name)
print('***********' + first_name + '***********')
print(first_name + '***********')
# I actually didn't understand the point, so I might have done sth wrong
# Here's another way:
first_name_2 = "***********" + first_name + "***********"
print(first_name_2.rstrip('***********'))
print(first_name_2)
print(first_name_2.lstrip('***********'))
# Question 15:
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
# Question 16:
print(name_one.islower())
print(name_two.isupper())
# if we want to check a specific character in name one we can use index:
# This is an example for checking the first character in name two
# print(name_two[0].isupper())
# Bonus:
# Question 17:
print(name_one.startswith('S'))
print(name_two.endswith("HD")) # This is case sensitive even if we check for ED not HD it will return false.
# Question 18:
msg = "I Love Python And Although I Love GSG with Zakaria"
print('Number of <Love> is: %d' % (msg.count('Love')))
print('Number of <t> is: %d' % (msg.count('t')))
# Question 19:
msg_2 = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg_2.replace('%7', 'Love', 1))
# Question 20:
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"

test1_len = len(test1)
if test1_len % 2 == 0:
    test1_half = int(test1_len/2)
    if test1[0:test1_half-1] == test1[test1_half:-1]:
        if test1[:] == test1[::-1]:
            print(f'{test1} is symmetrical, and {test1} is a palindrome.')
        else:
            print(f'{test1} is symmetrical, but {test1} is NOT a palindrome.')
    else:
        if test1[:] == test1[::-1]:
            print(f'{test1} is NOT symmetrical, but {test1} is a palindrome.')
        else:
            print(f'{test1} is NOT symmetrical, and {test1} is NOT a palindrome.')
else:
    if test1[:] == test1[::-1]:
        print(f'{test1} is NOT symmetrical, but {test1} is a palindrome.')
    else:
        print(f'{test1} is NOT symmetrical, and {test1} is NOT a palindrome.')

test2_len = len(test2)
if test2_len % 2 == 0:
    test2_half = int(test2_len/2)
    if test2[0:test2_half-1] == test2[test2_half:-1]:
        if test2[:] == test2[::-1]:
            print(f'{test2} is symmetrical, and {test2} is a palindrome.')
        else:
            print(f'{test2} is symmetrical, but {test2} is NOT a palindrome.')
    else:
        if test2[:] == test2[::-1]:
            print(f'{test2} is NOT symmetrical, but {test2} is a palindrome.')
        else:
            print(f'{test2} is NOT symmetrical, and {test2} is NOT a palindrome.')
else:
    if test2[:] == test2[::-1]:
        print(f'{test2} is NOT symmetrical, but {test2} is a palindrome.')
    else:
        print(f'{test2} is NOT symmetrical, and {test2} is NOT a palindrome.')

test3_clean = test3.replace(' ','').replace('.', '').lower()
test3_len = len(test3_clean)
if test3_len % 2 == 0:
    test3_half = int(test3_len/2)
    if test3_clean[0:test3_half-1] == test3_clean[test3_half:-1]:
        if test3_clean[:] == test3_clean[::-1]:
            print(f'{test3} is symmetrical, and {test3} is a palindrome.')
        else:
            print(f'{test3} is symmetrical, but {test3} is NOT a palindrome.')
    else:
        if test3_clean[:] == test3_clean[::-1]:
            print(f'{test3} is NOT symmetrical, but {test3} is a palindrome.')
        else:
            print(f'{test3} is NOT symmetrical, and {test3} is NOT a palindrome.')
else:
    if test3_clean[:] == test3_clean[::-1]:
        print(f'{test3} is NOT symmetrical, but {test3} is a palindrome.')
    else:
        print(f'{test3} is NOT symmetrical, and {test3} is NOT a palindrome.')

test4_len = len(test4)
if test4_len % 2 == 0:
    test4_half = int(test4_len/2)
    if test4[0:test4_half-1] == test4[test4_half:-1]:
        if test4[:] == test4[::-1]:
            print(f'{test4} is symmetrical, and {test4} is a palindrome.')
        else:
            print(f'{test4} is symmetrical, but {test4} is NOT a palindrome.')
    else:
        if test4[:] == test4[::-1]:
            print(f'{test4} is NOT symmetrical, but {test4} is a palindrome.')
        else:
            print(f'{test4} is NOT symmetrical, and {test4} is NOT a palindrome.')
else:
    if test4[:] == test4[::-1]:
        print(f'{test4} is NOT symmetrical, but {test4} is a palindrome.')
    else:
        print(f'{test4} is NOT symmetrical, and {test4} is NOT a palindrome.')


# The last code was tough, specially cuz u wanted the output to be in 1 line
# I tried my best but I am sure there's a better way
# I didn't attend the last 3 classes :( but I informed you about my traevlling situation
# However I only took a permission for 1 class as I didn't expect to not be able to attend the whole week.
# So please can you count me as an attendant? at least in the first one that I took permission for.
# Thank you a lot for everything so far ^^