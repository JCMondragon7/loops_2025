#notes on while loops
# for loops are for when u know exactly whne u wnat it to end, while loops are indefinate
#an infinite loop is yk
# name = input('enter your name')
# while name =='':
#     print('you did not enter your name')

# print(f'hello {name}')
# ---------------------------------------------
# age = int(input('enter in your age: '))

# while age < 0:
#     print('Age cant be negative')
#     age = int(input('enter your age: '))

# print(f'you are {age} years old')
# ---------------------------------------------------
# food = input('enter food you like (q to quit):')

# while not food == 'q':
#     print(f'you like {food}')
#     food = input('enter another food you like')

# print('bye')
#--------------------------------------------
# num = input('enter a # between 1 - 10: ')
# while num < 1 or num >10:
#     print(f'(num) is not valid')
#     num = int(input('enter a num between 1-10'))

# print(f'Your number is {num}')
# -------------------------------------
# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

index = 0

while index < len(colors):
    current_color = colors[index]
    if current_color == "yellow":
        break 
    print(current_color)
    index += 1