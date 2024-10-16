# print('Hello MohammadReza')
#
# print(18//4)
# print(3*5)
# print(10 % 4)   #Comments
#
# print("mehdi's Book")
# print('Moh',1,2.5)
# print('=' * 20)

import math
from math import factorial
from tokenize import String
from typing import FrozenSet

# print(factorial(10))


# a = 'abcdefghijklmnopqrstvuwxyz'
# print(a[-1 : -12 : -2])


# Name = 'Mehdi'
# Age = 33
#
#
#
# print('My Name is', Name , 'and my Age is' , Age)
# print('My Name is {} and my Age is {}' . format(Name,Age))


# for number in range(16):
    # print('{} ^ 2 = {}'.format(number,number ** 2))
# pi = 3.14258356544546541
# print(int(pi))
# # print(float('{:.2   f}'.format(pi)))
# # print(int(pi))
#
# print('My Nasm is mmmmm \n and my age is 18')
# Number= 46
#
# if Number % 3 == 0:
#     print('Hop')
# elif Number % 5 ==0:
#     print('Viz')
# else:
#     print(f'number is {Number}')

# String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in range(len(String)):
#     print(String[-i])


# for num in range(1,100):
#     if num %  3 == 0:
#         print('HOP')
#     elif num %  5 == 0:
#         print('WIZ')
#     else:
#         print(num)

#
#
#
# for i  in range(2,1000):
#         if i % i == 0 :
#             continue
# else:
#     print(i)
#
#
#
#
#
#         # if i % j != 0:
#         #     print(i)



# a = input('please enter an Integer: ' )
# b = 0
# c = 0
# while a != 'q' :
#     b = int(a) + b
#     c = c + 1
# print(b/c)

# if
# a = 'HopWiz' if

# print('=' * 48)



# for i in range(2,1000):
#     is_Prime = True
#     for j in (2 , i-1) :
#         if i % j == 0 :
#             is_Prime = False
#             break
#     if is_Prime :
#         print(i)


# a = 0
# b = []
# c = 0
# d= 0
# # print(type(a))
# while a != 1:
#     a = input('Please Enter a Number: ')
#     a = int(a)
#     b = b.append(a)
#     c = c + 1
#     continue
# else:
#     sum(b[0 : -1]) / (c-1)


AlphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for odd, even in zip(AlphabetString[::2], AlphabetString[1::2]):
#     print(odd , even)


# for index , i in AlphabetString:
# #     print(-index , i)
#
# print(AlphabetString[::-1])

#=========================

# a = 0
# b = 0
# c = 0
# # print(type(a))
# while a != 'q' :
#     a = input('Please Enter a Number: ')
#     if a.isdigit() :
#         a = int(a)
#         b = b + a
#         c = c + 1
#     else:
#         print(b // c)
#     continue
#
#
# ###########################
# print('=' * 40)
# print('Ali')

# a = 2802
# print(a in range(0 , 999999 , 1401))


# a = {
#     'Name' : 'MohammadReza' ,
#     'SurName' : 'Bagheri' ,
#     'Age' : 37
#     }
# # print(a['Name'])
#
# print(a.items())
# KeyList = list(a.items())
# print(KeyList)

#shar

# NumericString = '2,0.5874,-.23,0,1,25.358,39,100,358.1,5.0'
# Num = NumericString.rsplit(sep=',')
# a = 0
# for i in Num:
#     i = float(i)
#     a = a + i
# print(a)




#
# Numlist = list(Num)
# print(Numlist)

# a = 0
# NumList = NumList.append(print(NumericString,sep=','))
# for i in NumList:
#     a = a + i
# print(i)

#asdfb;lsfhdlk;segkbdsbpoaeds


string = ('Technology is changing rapidly, and innovations are transforming our daily lives.'
          ' Devices are more connected than ever,'
          ' and the internet was once a luxury but is now a necessity.'
          ' The world was simpler before smartphones, but today, they are essential tools.'
          ' Software advancements are making processes faster, '
          'and new developments were expected each year'
          '. As technology evolves, so are the ways we communicate and interact.')

a = ({'.'},{ },{','},{"'"})
SignSets = set(a)
# print(SignSets.intersection(String))


SignSets = frozenset(SignSets)
#mutable
for word in String:
    print(String.rsplit())


































#
# for i in range(1,100):
#     i = 'HopWiz' if i % 21 == 0 else 'Hop' if i % 3 == 0 else 'Wiz' if i % 7 == 0 else i
#     print(i)