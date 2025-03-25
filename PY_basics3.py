# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:10:57 2024

@author: dell
"""

# 1) Write a Python program to initialize a 3x3 NumPy array with any 
#integer values of your choice. Then, perform the following operations:
    
#Multiply the entire array by 2.    
#Add 5 to each element of the array.
#Calculate the square of each element in the array.
#Print the original array and the results of each operation.

# =============================================================================
# 
# import numpy as np
# 
# array = np.array([[1,2,3],[4,5,6],[7,8,9]])
# 
# Add_array = array+5
# Multiply_array = array*2
# Sqrt_array = np.square(array)
# 
# print(f"Original Array:", array)
# print(f"Adding 5 to each element of the array:",Add_array)
# print(f"Multiply the entire array by 2:", Multiply_array)
# print(f"The square of each element in the array:", Sqrt_array)
# 
# =============================================================================

# 2) Write a Python program to initialize a 3x3 NumPy array with any integer values of your choice. Then, perform the following slicing operations:
#Extract the first row of the array.
#Extract the last column of the array.
#Extract a 2x2 sub-array from the center of the original array.

# =============================================================================
# 
# import numpy as np
# 
# array = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(array)
# 
# print(array[0,:])
# print(array[:,2])
# print(array[1:3,1:3])
# 
# =============================================================================

# 3) Write a program to create a DataFrame in Python to store the names and marks of 10 students.
#  Each row of the DataFrame should represent a student, with columns as 'Name' and 'Marks'.
# Populate the DataFrame with appropriate data and then print it.

# =============================================================================
# 
# import pandas as pd
# Student_data = {
#         "Name": ["Chinmay", "Ritika", "Bhaskar", "Ravi", "Subrato", "Kaushalya", "Tanush", "Rashmi", "Mrunal",
#         "Kinnari"],
#         "Marks": [60, 50, 45, 55, 60, 75, 74, 39, 59, 50]
#         }
# df = pd.DataFrame(Student_data, index=[1,2,3,4,5,6,7,8,9,10])
# 
# print(df)
# 
# =============================================================================

# 4) Write a python program to create a DataFrame representing the names and income of 5 employees.
# The DataFrame should include columns ' Employee_name’ and ‘Income', and each row should correspond to an individual employee. 
# Use the indices 'a', 'b', 'c', 'd', and 'e' for the DataFrame entries to uniquely identify each employee.

# =============================================================================
# 
# import pandas as pd
# 
# Employee_data = {
#         "Emplayee_Name": ["Chinmay", "Bhaskar", "Ravi", "Subrato", "Tanush"],
#         "Income": [60000, 50000, 45000, 40000, 55000,]
#         }
# df = pd.DataFrame(Employee_data, index=["a","d","c","d","e"])
# 
# print(df)
# 
# =============================================================================

# 5) Imagine you're tasked with visualizing data using Python.
# You have the following dataset representing the frequency of occurrences for categories A, B, C, D, and E, stored in two lists:
# x = ['A', 'B', 'C', 'D', 'E']
# y = [10, 20, 15, 25, 30]
# Write a Python script that creates a bar plot to visualize this data. 
# The categories A, B, C, D, and E should be displayed on the x-axis, while the corresponding frequencies should be displayed on the y-axis.

# =============================================================================
# 
# import matplotlib.pyplot as plt
# 
# Categories = ['A', 'B', 'C', 'D', 'E']
# Frequencies = [10, 20, 15, 25, 30]
# 
# plt.bar(Categories, Frequencies, color = "blue")
# 
# plt.xlabel("Categories")
# plt.ylabel("Frequencies")
# plt.title("Bar Plot")
# 
# plt.show()
#
# =============================================================================
