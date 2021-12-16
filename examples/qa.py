# ASCII - 0-127
# index
name = 'Dima'
'''
D  | i | m | a
0  | 1 | 2 | 3
-4 |-3 |-2 | -1
'''

print(name[len(name) - 1])
print(name[-1])

######
# slices
# [start:end:step]
print('name[1:3]', name[1:3])
print('name[:3]', name[:3])
print('name[2:]', name[2:])
print('name[:]', name[:])
print('name[::2]', name[::2])
print('name[::-1]', name[::-1])
# anna
# ana
# s1 = 'anna'
# print(s1 == s1[::-1])

# print('name[]', name[3:-4:-1])  # comment
print('SLICE 3', name[10:100])
'''
D  i  m  a
0--------4
     2---4
              10 ----- 100
'''

# key1 = 'profile[name]'
# key1 = 'prof[company]'
# key1 = 'email'
#
# if '[' in key1:
#     print('left', key1[:key1.find('[')])
#     print('right', key1[key1.find('[')+1:-1])
# else:
#     print(key1)

# b = b'bytes'

# phone = '+38 (093) 546-45'
# phone = '+38 (093)54645'
# phone = '38-(093)-546x45'
#
# phone_clean = ''
# for char in phone:
#     if char.isdigit():
#         # phone_clean = phone_clean + char
#         phone_clean += char
#
# print(phone_clean)

# password > 8
# password < 31
# password should contain digit
# password should contain at least one lowercase
# password should contain at least one uppercase
print()
# password = '8569aaaaaac'
# if 8 < len(password) < 32:
#     contains_digit = False
#     contains_lowercase = False
#     contains_uppercase = False
#     for char in password:
#         if char.isdigit():
#             contains_digit = True
#         elif char.islower():
#             contains_lowercase = True
#         elif char.isupper():
#             contains_uppercase = True
#
#     if contains_digit and contains_lowercase and contains_uppercase:
#         print('valid')
#     else:
#         # breakpoint()  # import pdb;pdb.set_trace()
#         print('Invalid')
# else:
#     print('Invalid length')

# phone = '   +38093647526583   \n'
# print(phone.replace('+', '').strip())


# s1 = 'Hello World !'
# s2 = '/home/root/projects/main.py'
# print(s1.split())
# print(s2.split('/')[-1])

# url = 'users/list'
# url = 'users/delete'
# url = 'permissions/users/list'

'''
url.startswith('users/') start
'users' in url contains
url.endswith('users/') ends
'''

# if url.startswith('users/'):
# if 'users/' in url:
#     print('YES')

# name = 'Dima'
# age = 29

# text = 'Hello! My name is: ' + name + '. I am ' + str(age) + ' years old.'
# text = f'Hello! My name is: {name}. I am {age} years old.'
# text = 'Hello! My name is: {}. I am {} years old.'
# print(text.format(name, age))
# text = 'Hello! My name is: %s. I am %s years old.' % (name, age)
# print(text)

# money = 26.1234  # -> 26.12
# print(f'{money:.2f}')
