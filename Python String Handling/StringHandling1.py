# name = 'Om'
# age = 19

# # by using concat
# s1 = 'Hello ' + name + " Your Age is "+str(age)
# print(s1)

# # by using format function
# s2 = "Hello {0} Your Age is {1}".format(name, age)
# print(s2)

# # by using F-String
# s3 = f"Hello {name} Your Age is {age}"
# print(s3)
# print()
# print("##############################")
# print()
# String Methods


# s = "ThIs Is A PyThOn PRoJect 1"
# print(s.capitalize())  # Capitalize
# print(s.lower())  # Lower
# print(s.upper())  # Upper
# print(s.swapcase())  # SwapCase
# print(s.title())  # Title
# print(s.count('I'))  # Counting No. Of Repeated Occurrences
# print(s.endswith('.'))  # EndsWith
# print(s.startswith('T'))  # StartsWith
# print(s.find('o')) #Find
# print(s.index('T')) #Index
# print(s.rfind('A')) #R-Find
# print(s.rindex('A')) #R-index
# print("##############################")

# s1='hello123'
# print(s1.isalnum()) # All are alphanumeric or not
# print(s1.isalpha())# All are only alphabets or not
# print(s1.isdigit())# All are only digits or not
# print(s1.islower())# All are lower alphabets or not
# print(s1.isupper())# All are Upper Alphabets or not
# print(s1.isspace())# contains only void characters or not

# s2='OM'
# print(s2.center(10,'.'))
# print(s2.ljust(5,'.'))
# print(s2.rjust(5,'.'))

# s3='   Hello   Om   '
# print(s3.lstrip())
# print(s3.rstrip())

# s4='   Hello   Om   '
# print(s4.strip())

# if s3==s4:
#     print('Both Strings Spaces Are Removed....')
# else:
#     print('Not Equal')

s5 = 'This is Python Project 2'
arr_string = s5.split(' ')  # splitting into array of string

s6 = '-'.join(arr_string)  # joining with - to array
print(s6)
