
# # **Python Practice Problems (No Code Included)

# **Directions:** Solve each problem by writing your own Python code. Show outputs where required.


# # ### **Problem 1: Print Numbers 1 to 10

# # Write a program that prints the numbers from **1 to 10**, each on a new line.
# list1to10 = list(range(1,11))
# for number in list1to10:
#     print(number)



# # ### **Problem 2: Sum of Numbers

# # Ask the user for a number **n**, then calculate and display the **sum of all numbers from 1 to n**.
# n = int(input('enter a number: '))
# total_sum = 0
# for number in range(1, n+ 1):
#     total_sum += number

# print('the sum of numbers 1 to', n, 'is', total_sum)

# # ### **Problem 3: Factorial Calculator

# # Ask the user for a number **n**, then calculate the **factorial** of that number.

# # *(Example: factorial of 5 is 120)
# for i in range(10):
#     print(i)

# def factorial(n):

#     factorial = 1

#     for i in range(n):
#         factorial*=i+1

#     return factorial

# print(factorial(6))
# # ### **Problem 4: Count Vowels**

# # Ask the user for a string. Count and print how many **vowels (a, e, i, o, u)** are in the string.


# # ### **Problem 5: Print Even Numbers**

# # Ask the user for a number **n**, then print all **even numbers** from 2 up to n.
# n = int(input('Enter a number: '))
# print('even numbers from 2 to')
# for number in range(2, n + 1, 2):
#     print(number)

# listevennumbers = list(range(1,45))
# for number in listevennumbers:
# #if num even print
#     if number %2 == 0:
#         print('even number', number)
#     else:
#         print('odd number, skipping', number)


# # ### **Problem 6: Reverse a String**

# # Ask the user for a string, then print the string **backwards**.
# name = input('enter a string: ')
# reversed_name = ''
# for char in name:
#     #we are looing through characters
#     #n adding to front of reversed_name
#     reversed_name = char + reversed_name
# #prepend each character to rever name
# print('reversed string', reversed_name)
# print(reversed_name[::-1])#alt method usin slicing


# ### **Problem 7: Multiplication Table**

# Ask the user for a number **n**, then print the **multiplication table** for n from
# n × 1 up to n × 10.



# ### **Problem 8: Count Occurrences**

# Ask the user for **two strings**, a and b.
# Determine how many times **string b appears inside string a**.



# ### **Problem 9: Fibonacci Sequence**

# Ask the user for a number **n**, then print the first **n numbers** of the Fibonacci sequence.
#reccursion means a function called itself
def carprice(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return carprice(n - 1) + carprice(n - 2)
print(carprice(6)) #output 8

def fibonacci(n):

    if n in [1,2]:
        return 1
    
    return fibonacci(n-1)+fibonacci(n+2)

for i in range(1,10):
    print(fibonacci(i))



# ### **Problem 10: Pattern Printing**

# Ask the user for a number **n**, then print a pattern of stars where the first row has 1 star, the second has 2, and so on until row n.

# *(Example for n = 4)*
# *
# **
# ***
# ****



# If you want, I can also turn this into a **Google Doc**, **worksheet**, **PDF**, or **Canvas/Schoology assignment format**.
