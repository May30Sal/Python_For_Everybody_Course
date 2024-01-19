import math #built-in module, don't need to install using pip package manager
import numpy as np
# import pandas as pd - Has to be installed too
from math import pi

#! Examples of usage of the libraries math and numpy
#print(math.pi)
#print(math.sqrt(4))
#b = np.full((2,10), 1)
#print(b)

#! creating a dict
# employee_dict = {'first_name': str(name), 'age': int(age), 'title': str(title)}
# return employee_dict

#! The full() function creates a two-dimensional matrix of dimensions 2 x 10 consisting only of the values 1

#! If you want u can use only one or 2 functions from the module it's easier and save space if u only 
#! import the function u want: for example,from math import sqrt, cos - and them use it as sqrt(4) without the math.


#! BOOK PYTHON FOR EVERYBODY

#! Exercises - Chapter 2 - Variables, expressions, and statements


#! Exercise 1
# name = input("What's your name: \n")
# print ("Hello,", name)

#! Exercise 2
# width = 17
# height = 12.0

# print(width // 2)
# print(width / 2.0)
# print(height / 3)
# print(1 + 2 * 5


#! Exercise 3
# tempC = input("Type the tempretaure in C: ")
# tempF = (float(tempC) * 1.8) + 32
# print(round(tempF, 2), "F")


#! Exercises - Chapter 3 - Conditional execution

#! Exercise 1 & 2
# while True: 
#     hours = input("Enter hours: ")
#     rate = input("Enter rate: ")

#     try:
#         if (float(hours) > 40):
#             totalPay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5 ))
#             print("Total Pay: ", totalPay)
#         else:
#             totalPay = float(hours) * float(rate)
#             print("Total Pay: ", totalPay)
#         break
#     except:
#         print("Error, please enter numeric input")


#! Exercise 2
# score = input("Enter score: ")

# try: 
#     if (float(score) <= 1.0) and (float(score) >= 0.9):
#         print("A")
#     elif (float(score) >= 0.8) and (float(score) < 0.9):
#         print("B")
#     elif (float(score) >= 0.7) and (float(score) < 0.8):
#         print("C")
#     elif (float(score) >= 0.6) and (float(score) < 0.7):
#         print("D")
#     elif float(score) < 0.6:
#         print("F")
#     else:
#         print("Bad score")
# except:
#     print("Bad score")


#! Exercises - Chapter 4 - Functions

#! Exercise 6
# hours = input("Enter hours: ")
# rate = input("Enter rate: ")

# def computepay(hours, rate):
#     try:
#         if (float(hours) > 40):
#            totalPay = (40 * float(rate)) + ((float(hours) - 40) * (float(rate) * 1.5 ))
#            return totalPay
#         else:
#             totalPay = float(hours) * float(rate)
#             return totalPay
#     except:
#         print("Error, please enter numeric input")

# p = computepay(hours, rate)
# print(p)

# for i in range(10):
#     x = random.random()
#     print(x)

#! Exercise 7
# score = input("Enter score: ")

# def computeGrade(score): 
#     if (float(score) <= 1.0) and (float(score) >= 0.9):
#         return("A")
#     elif (float(score) >= 0.8) and (float(score) < 0.9):
#         return("B")
#     elif (float(score) >= 0.7) and (float(score) < 0.8):
#         return("C")
#     elif (float(score) >= 0.6) and (float(score) < 0.7):
#         return("D")
#     elif float(score) < 0.6:
#         return("F")
#     else:
#         return("Bad score")

# print(computeGrade(score))


#! Exercises - Chapter 5 - Iteration

#! Exercise 1
# listnum = []

# while True:
#     number = input("Enter a number: ")
#     try:
#         if number == "done":
#             print("done")
#             break
#         else:
#             # number == int(number)
#             listnum.append(int(number))
#     except:
#         print("Invalid input")
# sumarray = sum(listnum)
# count = len(listnum)
# avg = sumarray / count
# print(sumarray, count, avg)

# totnum = 0
# sumnum = 0

# #! Teacher solution
# while True:
#     number = input("Enter a number: ")
#     try:
#         if number == "done":
#             break
#         else:
#             newnumber = float(number)
#             totnum = totnum + 1
#             sumnum = sumnum + newnumber    
#     except:
#         print("Invalid input")
# print(totnum, sumnum, totnum / sumnum)

#! Extra - Graded Assignment
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         print(num)
#         break
#     try:
#         num = float(num)
#         largest = num if largest is None else max(num, largest)
#         smallest = num if smallest is None else min(num,smallest) 
#     except:
#         print("Invalid input")
# print("Maximum is ", largest)
# print("Minimum is ", smallest)


# largest = num if largest is None else max(num, largest)
# smallest = num if smallest is None else min(num,smallest)

#! Exercise 2
# listnum = []

# while True:
#     number = input("Enter a number: ")
#     try:
#         if number == "done":
#             print("done")
#             break
#         else:
#             # number == int(number)
#             listnum.append(int(number))
#     except:
#         print("Invalid input")
# minumber = min(listnum)
# maxnumber = max(listnum)
# print(minumber, maxnumber)


#! Exercises - Chapter 6 - Strings

#! Exercise 5

#text = "X-DSPAM-Confidence:    0.8475"
#number = text.find('0')
#print(number)
#print(float(text[number:]))



#file = open('G:\My Drive\Programming\Learning_Python/lorem.txt' , 'r')
#file_list = []
#for line in file.readline():
#    print(line)
#file.close()

#! Exercise 1

#word = 'marrakesh'
#count = len(word) - 1

#while count >= 0:
#    print(word[count])
#    count = count - 1

# #! Exercise 3

# def countLetter(letter, word):
#     count = 0
#     for i in word:
#         if i == letter:
#             count = count + 1
#     print(count)

# countLetter('l', 'balacobaco')

# nome = 'bananana'
# #print(nome.capitalize()) #! String Methods 

# #! Exercise 4
# print(nome.count('a'))


# fname = input("Enter file name: ")
# fh = open(fname)
# inp = fh.read()
# print(inp.rstrip().upper())

# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# total = 0
# spamct = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     total = total + 1
#     spam = line[20:].strip()
#     spamct = spamct + float(spam)
# avg = spamct / total
# print("Average spam confidence:", avg)

#! Exercises - Chapter 7 - Files

#! Creating and reading files
#with open('newfile.txt', 'w') as file:
# file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nDonec ut sodales risus. Maecenas fermentum nulla ac sem viverra fringilla. Suspendisse eget mauris eget arcu porta varius.\nSed auctor ultrices mauris a sodales. Sed imperdiet eu elit sit amet semper. Duis elementum ante in lacus lobortis, faucibus pellentesque purus finibus.\nPhasellus nec lacus ac metus auctor aliquet. Morbi ac turpis at felis condimentum congue id at nisl. Curabitur a commodo augue, non elementum lorem.\nPellentesque dignissim, risus ultrices interdum feugiat, magna orci maximus purus, eget gravida libero nisl vitae odio.\nCras urna velit, dignissim vitae pellentesque id, mollis sit amet lectus. Sed imperdiet massa arcu, ac placerat risus tincidunt ac.\nNulla luctus mauris dolor, ac faucibus felis pulvinar ut.")

#file = open('newfile.txt', mode='r')
#data = file.readlines()
#print(data)
#file.close()

#! counting # of lines
#file = open('newfile.txt')
#count = 0
#for line in file:
#   count = count + 1
#print(count)

#data = file.read()
#print(len(data))
#print(data[:50]) #! slice the string and print from the start until the caracter # 50 (ele inclusive)

#for line in file:
#   if line.startswith("Sed"):
#      print(line)

#! open the file to write in it 'w' (will overcome what was written before if the file exists, or create a new one)
#file = open('newfile.txt', 'w')
#file.write("teste\n")
#file.write("mais um teste\n") #! since it's opened, the new lines will be end at the end
#file.close()
#! open the file to append a text to the end of it 'a', because it was closed before
#file2 = open('newfile.txt', 'a')
#file2.write("continuando")
#! close the file
#file2.close()
#! open the file to read it (it has to be created as variables!)
#data = open('newfile.txt', 'r')
#line = data.read().upper() #! reading the file in Upper Case
#print(line)
#! creating a list out of the file
#data = open('newfile.txt', 'r')
#data2 = data.read()
#data3 = data2.split()
#print(data3)
#! function that returns all the spaces and newlines as carateres, helpful for debugging
#print(repr(line))


#! Exercises - Chapter 8 - Lists

#! creting a list
#fruit_list = ['apple', 'orange', 'banana', [2, 5.0]]
#print(fruit_list)
#print(fruit_list[2])
#print(len(fruit_list))
#! acessing an intem insite the nested list
#print(fruit_list[3][0])

#! going through the list with a for loop
#for i in fruit_list:
#    print(i)

#! list methods
#fruit_list.append('cherry') #!adds one item
#fruit_list.pop(3)  #! extract the item by its index
#fruit_list.remove('banana') #! extract the item by its name
#fruit_list.sort() #! sort the list from low to high
#print(fruit_list)

#! creating a list from a string
#i = 'love'
#t = list(i) #! list is a built-in function that creates a list
#print(t)

#! differences between values and objects
#a = [1,2,3]
#b = [1,2,3]
#print(a is b) #! answer is False, because they are different objects with the same value
#c = a
#print(c is a) #! anser is True, bc in this case both a and c points to the same object. So changing one will change both.

#! Exercise 1
#i = [1,2,3]

#def chop(t):
#    del t[0]
#    t.pop()

#def middle(t):
#    del t[0]
#    t.pop()
#    x = t
#    return x

#print(middle(i))

#! Exercise 4
# with open ('romeo.txt', mode='r') as file:
#     data = file.read()
#     romeo = data.split()
#     unique = []
#     for word in romeo:
#         if word not in unique:
#             unique.append(word)
#     unique.sort()
#     print(unique)

#! Exercise 5
# total = 0
# unique_mail = []
# with open('mbox.txt', mode = 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             sender = line.split()
#             if sender[1] not in unique_mail:  #! Extra operation to save only the unique emails on a list!
#                 unique_mail.append(sender[1])
#             #print(sender[1])
#             #total = total + 1
# #print(total)
# print(unique_mail)
# print(len(unique_mail))

#! Exercise 6
# numbers = []
# number = input("Tell me a number: ")
# while number != 'done':
#     numbers.append(number)
#     number = input("Tell me a number: ")
# minimo = min(numbers)
# maximo = max(numbers)

# print(float(minimo))
# print(float(maximo))


    
#! OOP examples

# Inheritance
#class A:
#   a = 1

#class B:
#   b = 2
   
#class C(A, B): #! Inherits from classes A and B
#   pass

#c = C()
#print(c.a,'\n', c.b)

#num = 9
#class Car:
#    num = 5
#    bathrooms = 2

#def cost_evaluation(num):
#    num = 10
#    return num

#class Bike():
#    num = 11

#class A:
#   def a(self):
#       return "Function inside A"

#class B:
#   def a(self):
#       return "Function inside B"

#class C:
#   pass

#class D(C, A, B):
#   pass

#d = D()
#print(d.a())

