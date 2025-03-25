# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:07:14 2024

@author: dell
"""

# 1) Write a program that prompts the user to input a year, checks whether it's a leap year or not, and then prints the result.
# =============================================================================
# 
# year= int(input("Enter year:"))
# 
# if (year% 4 == 0 and year % 100!= 0) or (year % 400 ==0):
#     print("Its a Leap Year")
# else:
#     print("Its not a Leap year")
#     
# =============================================================================

# 2) Write a Python program that prompts the user to input a word.
# The program should then determine and output the count of vowels (a, e, i, o, u) in the provided word. Additionally, 
# consider that the word can be in either uppercase or lowercase.
# =============================================================================
# 
# Word = input("Enter a Word:")
# 
# vowel_count = 0
# vowel= {'a','e','i','o','u','A','E','I','O','U'}
# for char in Word:
#     if char in vowel:
#         vowel_count +=1
#         
# print(f"The count of vowels in '{Word}' is '{vowel_count}'")
# 
# =============================================================================


# 3) Write a Python program that allows the user to input a list of 6 names. 
# After receiving the list, the program should print only the names that start with the letter 'a', regardless of whether the letter is uppercase or lowercase.

# =============================================================================
# 
# def name_starting_with_a (Names):
#     print('Name Starting with "a":')
#     for name in Names:
#         if name.startswith("a"):
#             print(name)
# num_Names= 6
# Names=[]
# for i in range (num_Names):
#     name = input("Enter Name:").lower()
#     Names.append(name)
#     
# name_starting_with_a(Names)
#
# =============================================================================

# 4) Write a Python program that takes a list of 10 integers as input. Your program should iterate through the list and print the following:
# For each even number encountered, print the number squared.
# For each odd number encountered, print the number cubed.

# =============================================================================
# 
# def check_number_even_or_odd(number):
#     for num in number:
#         
#         if num %2==0:
#             print("It is an even number.",num**2)
#         else:
#             print("It is an odd number.",num**3)
#         
# number =[]        
# for i in range(10):
#     num = int(input("Enter a Number"))
#     number.append(num)
#     check_number_even_or_odd(number)
#
# =============================================================================

# 5) Imagine you're ordering flowers from a local delivery service. 
# They offer a selection of beautiful flowers, including roses. 
# Each rose is priced at Rs. 10. Along with your choice of roses, you'll need to provide the count of roses you wish to order and the delivery distance.
# The delivery charges are as follows: Rs. 25 for distances within 5 kilometers, Rs. 50 for distances between 5 and 10 kilometers, and Rs. 75 for distances greater than 10 kilometers. 
# Write a Python program that prompts the user to enter the count of roses and the delivery distance, then calculates and displays the total price to pay, including both the cost of roses and the delivery charge.

# =============================================================================
# 
# def to_calculate_delivery_cost(distance):
#     if distance<=5:
#         return 25
#     elif distance<=10:
#         return 50
#     else:
#         return 75
# 
# rose_price = 10
# 
# number_of_rose = int(input("Enter the number of rosses to order:"))
# 
# distance_to_deliver= float(input("Enter the distance:"))
# 
# rose_cost = number_of_rose* distance_to_deliver
# 
# delivery_cost = to_calculate_delivery_cost(distance_to_deliver)
# 
# total_cost = delivery_cost+ rose_cost
# 
# print(f"Toatl price to be paid : {total_cost}")
# 
# =============================================================================




        