# import math #built-in module, don't need to install using pip package manager
# import numpy as np
# import pandas as pd - Has to be installed too
# from math import pi
import re

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

#! Exercises - Chapter 9 - Dictionaries

#! Exercise 1 (creating a dict with words in a file)
# words = {}
# with open('romeo.txt', 'r') as file:
#     for line in file:
#         word = line.split()
#         for i in word:
#             if i not in words:
#                 words[i] = 1
#             else:
#                 words[i] += 1
        
# print(words)
# print('But' in words)  #! It is case sensitive! 


# #! This will return the value corresponding to the key 'Also', 
# #! and if it doesn't exist will return the default value we set, 0 in this case
# print(words.get('Also', 0))

# #! Exercise 2
# counts = dict()
# with open('mbox-short.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             if words[2] not in counts:
#                 counts[words[2]] = 1
#             else:
#                 counts[words[2]] += 1
# print(counts)

#! Exercise 3
# counts = dict()
# with open('mbox-short.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             if words[1] not in counts:
#                 counts[words[1]] = 1
#             else:
#                 counts[words[1]] += 1
# print(counts)

#! Challenge - Exercise 4
# counts = dict()
# with open('G:\My Drive\Programming\Learning_Python\PYE\mbox.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             if words[1] not in counts:
#                 counts[words[1]] = 1
#             else: 
#                 counts[words[1]] += 1
# print(counts)

# max_key = None
# max_val = None

# for key, val in counts.items():

#     if max_val is None or val > max_val:
#         max_val = val
#         max_key = key

# print(max_key, max_val)

#! 2nd way:
# counts = dict()
# with open('G:\My Drive\Programming\Learning_Python\PYE\mbox.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             for w in words:     
#             #    print(w) #! Print just the words
#                 if words[1] not in counts:
#                  counts[words[1]] = 1
#                 else: 
#                  counts[words[1]] += 1
# print(counts)

#! 3rd way using get() method:
# counts = dict()
# with open('G:\My Drive\Programming\Learning_Python\PYE\mbox.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             for w in words:
#                 counts[words[1]] = counts.get(words[1], 0) + 1 
#             #! Get in the dict "counts" the word if it doesn't exist and set its value to 0
# print(counts)


#! Exercise 5 - get in a dict only the domain name and the count of how many emails they send
# counts = dict()
# with open('G:\My Drive\Programming\Learning_Python\PYE\mbox.txt', 'r') as file:
#     for line in file:
#         if line.startswith('From '):
#             line.rstrip()
#             words = line.split()
#             domain = words[1].rsplit('@')
#             if domain[1] not in counts:                       
#                 counts[domain[1]] = 1
#             else: 
#                 counts[domain[1]] += 1
# print(counts)      

#! Getting the dict values and putting them in a list
# fruits = {'apple': 1, 'banana': 2, 'orange': 3 }
# num = []
# for i in fruits.values():
#     num.append(i)
# print(num)

#! Getting the dict keys and putting them in a list
# fruitslist = []
# for fruit in fruits:
#     fruitslist.append(fruit)
# print(fruitslist)


#! Exercises - Chapter 10 - Tuples
# creating a tuple from a dict, then sorting it as a list
# groceries = {'rice': 1, 'beans': 2, 'meat': 5, 'butter': 3}
# update = list(groceries.items())
# update.sort()
# print(type(update)) #dict items = tuple
# print(update)

# Methods that reverse and sort the order of the dict items
# print(list(reversed(groceries.items())))
# print(list(sorted(groceries.items())))

#creating a dict from a tuple and updating it
# newlist = dict()
# for x, y in groceries.items():
#     y = y + 1
#     newlist[x] = newlist.get(x, y)
#     print(newlist)
    

# For loop through the dict and update values
# for k, v in list(groceries.items()):
#     v = v + 1
#     print(k,v)
#     print(v, k)

# For loop through the dict, create a list and sort values
# l = list()
# for k, v in list(groceries.items()):
#     l.append((v, k)) # Needs to put inside parenthesis to append it!

# l.sort(reverse=True)
# print(l)

#! Exercise 1
# Opening the file
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# counts = dict()
# for line in handle:
#     if line.startswith('From '):
#         line.rstrip()
#         words = line.split()
#         # print(words) # To see that when u split and put into a variable, u get words instead or caracteres!
#         # print(words[5][:2]) # Slice to get only the first 2 numbers (hour)
#         counts[words[1]] = counts.get(words[1], 0) + 1  

# # Creating a list and appending the values and keys in this order
# t_email = list()
# for k, v in list(counts.items()):
#     t_email.append((v, k))


# # sorting the list in reverse order of values, and accesing the value-key
# t_email.sort(reverse=True)
# print(t_email[0][1], t_email[0][0])

#! Challenge -  Exercise 2
# Opening the file
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# counts = dict()
# for line in handle:
#     if line.startswith('From '):
#         line.rstrip()
#         words = line.split()
#         # print(words) # To see that when u split and put into a variable, u get words instead or caracteres!
#         # print(words[5][:2]) # Slice to get only the first 2 numbers (hour)
#         counts[words[5][:2]] = counts.get(words[5][:2], 0) + 1  

# sorted_list = list(counts.items())
# sorted_list.sort()

# for k, v in sorted_list:
#     print(k, v)

# # other way to print
# print(sorted([(k, v) for k, v in counts.items()])) # as a list

# for k, v in sorted([(k, v) for k, v in counts.items()]):  # as items
#     print(k, v)

#! Exercise 3 (I changed to uppercase, since my text was already in lowercase)
# import string

# name = input("Enter file:")
# if len(name) < 1:
#     name = "romeo.txt"
# handle = open(name)

# counts = dict()
# for line in handle:
#     line.rstrip()
#     line.split()
#     line = line.upper() # To make all letters uppercase, since python counts them as different things
#     for letter in line:
#         if letter.isalpha(): # To return only alphabetical caracteres
#             counts[letter] = counts.get(letter, 0) + 1

# order_letters = list()            
# for k, v in list(counts.items()):
#     order_letters.append((v, k)) # Transform to UpperCase
#     order_letters.sort(reverse=True)

# print(order_letters)


#! Exercises - Chapter 11 - Regex

# s = '67n teste@gmail.com sji09'
# x = re.findall('\S@\S+', s) #Will get only e@gmail.com
# y = re.findall('\S+@\S+', s) #Will get the entire email
# print(x)
# print(y)

#! Exercise 1 - without asking for a user input
# count = 0
# with open ('mbox.txt', mode='r') as file:
#     for line in file: 
#         line.rstrip()
#         data = re.findall('^Author', line)
#         if len(data) > 0:
#             count = count + 1
# print(count)

#! Asking for the user input
# name = input("Enter a regular expression: ")
# count = 0
# with open ('mbox.txt', mode='r') as file:
#     for line in file: 
#         line.rstrip()
#         data = re.findall(name, line)
#         if len(data) > 0:
#             count = count + 1
# print('mbox.txt had {} lines that matches {}'.format(count, name))

# #! Exercise 2 

# data_list = []
# nums = []
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# for line in handle:
#     line.rstrip()
#     data = re.findall('^New.*: ([0-9][0-9][0-9][0-9][0-9])', line)
#     if len(data) > 0:
#         data_list.append(data)


# for x in data_list:
#     y = ''.join(x) #! converting list into string
#     nums.append(int(y))


# print(sum(nums) / len(nums))

#! Challenge 
# data_list = []
# nums = []
# count = 0
# with open ('actual_file.txt', mode='r') as file:
#     for line in file:
#         line.rstrip()
#         data = re.findall('[0-9]+', line) # ou '\d+' to find the digits
#         for num in data:
#             y = ''.join(num) #! converting list into string
#             nums.append(int(y)) #! converting list into int
#             count = count + 1

# #print(nums)
# print(count)
# print(sum(nums))


#! Exercises - Chapter 12 - Networked Programs

#! Using socket
import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# mysock.close()

#! Exercise 1 (Need to fix it)

#Ask for a user input and split it to get the host name
# page = input('Enter a web page - ')
# add = page.split('/')
# try:
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((add[2], 80))
#     spot = str(page) #Get the entire input URL 
#     cmd = ('GET {} HTTP/1.0\r\n\r\n'.format(spot)).encode()
#     mysock.send(cmd)
#     while True:
#         data = mysock.recv(512)
#         if len(data) < 1:
#             break
#         print(data.decode(), end='')

#     mysock.close()

# except:
#     print('This is not a valid URL')

#! Exercise 2
# page = input('Enter a web page - ')
# add = page.split('/')
# try:
#     mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     mysock.connect((add[2], 80))
#     spot = str(page) #Get the entire input URL 
#     cmd = ('GET {} HTTP/1.0\r\n\r\n'.format(spot)).encode()
#     mysock.send(cmd)
#     while True:
#         data = mysock.recv(512)
#         if len(data) < 1:
#             break
#         print(data.decode(), end='')

#     mysock.close()

# except:
#     print('This is not a valid URL')


# #! Parsing and web scraping
# from bs4 import BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# import ssl

# #Ignore SSL Certificate Errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# # print(soup) #will print all the html in the page

# #Retrieve a specific string, exaple: all the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

#! Challenge 1
# from bs4 import BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# import ssl

# num_list = []
# #Ignore SSL Certificate Errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# #Retrieve the numbers
# spans = soup('span')
# for span in spans:
#     num_list.append(int(span.contents[0])) #Get the content on the tag

# print(len(num_list))
# print(sum(num_list))
    

#! Challenge 2
# from bs4 import BeautifulSoup
# import urllib.request, urllib.parse, urllib.error
# import ssl

# #Ignore SSL Certificate Errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# #Ask user input
# url = input('Enter URL: ')
# count = input('Enter count: ')
# position = input('Enter position: ')

# new_count = int(count)
# while new_count > 0:
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     for tag in tags:
#         new_link = tags[int(position)].get('href', None)
    
#     new_count = new_count - 1
#     url = new_link
#     print(new_link)


#! Chapter 13 - Using Web Services

#! Challenge 1 XML
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET

# #Ask user input
# url = input('Enter URL: ')

# fhand = urllib.request.urlopen(url)
# data = fhand.read()
# tree = ET.fromstring(data)
# counts = 0

# for item in tree.findall('.//count'):
#     counts = counts + int(item.text)

# print(counts)

#! Exercise 1 jSON
# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# Important: As of January, 2024 this course no longer includes
# The use of Google's Geocoding API in the content.   This
# has been replaced by OpenStreetMap data
# See the file opengeo.py

# This file is here for previous versions of the course
# materials and since it uses a proxy server to access the API,
# it should work for a while.

#print("See https://www.py4e.com/code3/opengeo.py")

# api_key = 42
# serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


#     try: 
#         country = js['results'][0]['address_components'][3]['short_name']
#         country2 = js['results'][0]['address_components'][3]['long_name']
#         print(country)
#         print(country2)
#     except:
#         print('Not a country or Index error')
#     break

#! Challenge 2 JSON
# import json
# import urllib.request, urllib.parse, urllib.error
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# counts = 0

# while True:
#     url = input('Enter url: ')
#     if len(url) < 1: break

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.loads(data)
#         for item in js['comments']:
#             counts = counts + item['count']
#     except:
#         js = None
#     break

# print(counts)


#! Example
# import urllib.request, urllib.parse
# import json, ssl

# # Heavily rate limited proxy of https://www.geoapify.com/ api
# serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     address = address.strip()
#     parms = dict()
#     parms['q'] = address

#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'features' not in js:
#         print('==== Download error ===')
#         print(data)
#         break

#     if len(js['features']) == 0:
#         print('==== Object not found ====')
#         print(data)
#         break

#     # print(json.dumps(js, indent=4))

#     lat = js['features'][0]['properties']['lat']
#     lon = js['features'][0]['properties']['lon']
#     print('lat', lat, 'lon', lon)
#     location = js['features'][0]['properties']['formatted']
#     print(location)

#! Challenge 3 JSON
# import urllib.request, urllib.parse
# import json, ssl

# # Heavily rate limited proxy of https://www.geoapify.com/ api
# serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     address = address.strip()
#     parms = dict()
#     parms['q'] = address

#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'features' not in js:
#         print('==== Download error ===')
#         print(data)
#         break

#     if len(js['features']) == 0:
#         print('==== Object not found ====')
#         print(data)
#         break

#     # print(json.dumps(js, indent=4))

#     plusCode = js['features'][0]['properties']['plus_code']
#     print(plusCode)
#     break


#! Chapter 14 - Object Oriented Programming

# class PartyAnimal:

#    def __init__(self):
#      self.x = 0

#    def party(self) :
#      self.x = self.x + 1
#      print("So far",self.x)

# an = PartyAnimal()
# an.party()
# an.party()
# an.party()


#! Other OOP examples

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

#! Chapter 15 - Database 
#! Challenge Week 2

# import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '): continue
#     pieces = line.split()
#     longEmail = pieces[1].split('@')
#     email = longEmail[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (email,))
#     conn.commit()

# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()


#org = re.findall('\@\S+', email)

#! Chapter 15 - Database 
#! Challenge Week 3

# import sqlite3

# conn = sqlite3.connect('tracks.sqlite') # creating the database name tracks
# cur = conn.cursor() # it's like the file handler to the database server

# # creating the tables
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
# DROP TABLE IF EXISTS Genre;
                                    
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY 
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''')

# # reading the csv or json file
# fh = open('tracks.csv')
# for line in fh:
#     line = line.strip()
#     pieces = line.split(',')
#     if len(pieces) < 6 : continue

#     name = pieces[0]
#     artist = pieces[1]
#     album = pieces[2]
#     count = pieces[3]
#     rating = pieces[4]
#     length = pieces[5]
#     genre = pieces[6]

#     print(name, artist, album, count, rating, length, genre)

#     # inserting the values of the file in the database tables
#     # the ignore is like an error handling, It makes sure that if a particular title is already in the table, 
#     # there are no duplicate rows inserted
#     cur.execute('''INSERT OR IGNORE INTO Artist (name) 
#         VALUES ( ? )''', ( artist, ) )
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#     artist_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Genre (name) 
#             VALUES ( ? )''', ( genre, ) )
#     cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
#     genre_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, genre_id, len, rating, count) 
#         VALUES ( ?, ?, ?, ?, ?, ? )''', 
#         ( name, album_id, genre_id, length, rating, count ) )

#     conn.commit()

    
#! Chapter 15 - Database 
#! Challenge Week 4

# import json
# import sqlite3

# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()

# # Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER PRIMARY KEY,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER PRIMARY KEY,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')

# # fname = input('Enter file name: ')
# # if len(fname) < 1:
# fname = 'roster_data.json'

# #   [ "Charley", "si110", 1 ],
# #   [ "Mea", "si110", 0 ],

# str_data = open(fname).read()
# json_data = json.loads(str_data)

# for entry in json_data:

#     name = entry[0]
#     title = entry[1]
#     role = entry[2]

#     #print((name, title, role))

#     cur.execute('''INSERT OR IGNORE INTO User (name)
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR IGNORE INTO Course (title)
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]

#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id, role) VALUES ( ?, ?, ? )''',
#         ( user_id, course_id, role ) )

#     conn.commit()
