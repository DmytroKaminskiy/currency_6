# [0 - 100]

# for num in range(101):
#
#     if num % 15 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)

# break_out = False
#
# for i in range(10):
#
#     for j in range(10):
#         if i == 5 and j == 5:
#             break_out = True
#             break
#         print(i, j)
#
#     if break_out:
#         break

# counter = 0
# while counter != 10:
#     counter += 1
#
#     if counter % 2 == 1:
#         continue
#
#     print(counter)
#
#     ...
# else:
#     print('ELSE')

# while True:
#     num1 = input('Enter first number: ')
#     if num1 == 'q' or num1 == 'quit':
#         break
#
#     num1 = int(num1)
#     operation = input('Enter operation: ')
#     num2 = int(input('Enter second number: '))
#     print(num1, operation, num2)
#
#     if operation == 'plus':
#         print(num1 + num2)
#     elif operation == 'minus':
#         print(num1 - num2)
#     else:
#         print('Operation', operation, 'not found')

# if flag:
#     x = str(2 + 2 * 2)
# else:
#     if flag2:
#         x = str(2 + 3 * 2)
#     else:
#         x = str(4 + 2 * 4)

# flag = False
# flag2 = True

# x = str(2 + 2 * 2) || if flag else || str(4 + 2 * 4)
# x = str(2 + 2 * 2) || if flag else || str(2 + 3 * 2) || if flag2 else || str(4 + 2 * 4)
# x = str(2 + 2 * 2) if flag else str(2 + 3 * 2) if flag2 else str(4 + 2 * 4)

# x2 = [str(2 + 2 * 2) for i in range(20) if i % 2 == 0]
# print(x)
