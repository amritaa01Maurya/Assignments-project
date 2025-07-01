# # assignment 

# import math

# def squareRoot():
#     try:
#        num = float(input("Enter a number: "))
#        if num >= 0:
#               return math.sqrt(num)
#        else:
#               raise Exception("Square root of negative number is not possible")
#     except ValueError:
#         print('Please enter a valid number')
#     except Exception as e:
#         print('Unexpected Error', e)
#     finally:
#         print("Calculation done.") 

# print(squareRoot())

# homework we have make 2d matrix
#   x1   x2  x3
#   10  20  30 
#   14  24  34
#   16  26  36


# we have to store data in txt as 
# x1, x2, x3
# 10, 20, 30
# 14, 24, 34 
# 16, 26, 36

arr = [['x1','x2', 'x3'],
       [10, 20, 30],
       [14, 24, 34],
       [16, 26, 36]
]

# with open('assignment1.csv','w') as file:
#     for i in arr:
#        for j in i:
#               file.write(str(j) + ', ')  # 10, 20, 30,
       
#        file.write('\n')

       # OR

with open('assignment1.csv','w') as file:
    for i in arr:
        file.write(', '.join(map(str,i)) + '\n') # 10, 20, 30