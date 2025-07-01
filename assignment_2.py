# Numpy Questions
import numpy as np

# task 1
# n1 = np.arange(1,11,1)
# print(n1)
# print(n1.shape,n1.size,n1.dtype)

# n2 = np.arange(1,10,1).reshape(3,3)
# print(n2)
# print(n2.shape,n2.size,n2.dtype)

# n3 = np.random.random(size = (3,5,3))
# print(n3)
# print(n3.shape,n3.size,n3.dtype)

# task 2
# data = [10, 20, 30, 40, 50, 60, 70, 80, 90] 

# n1 = np.array(data)
# print(n1[:3])
# print(n1[::2])
# print(n1[::-1])

# task 3
A = np.random.randint(1,20,(5))
B = np.random.randint(1,20,(5))
# print(A,B)
# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)

# print(A@B)

# print(np.mean(A))
# print(np.median(A))
# print(np.std(A))
# print(np.var(A))

# print(np.max(B),np.argmax(B))
# print(np.min(B),np.argmin(B))

# task 4
# n1= np.arange(1,13)

# n2 = n1.reshape(4,3)
# print(n2)
# print(n1.reshape(2,2,3))
# print(n2.transpose())

# task 5

# n1 = np.random.randint(10,50,(15))
# print(n1)

# print(n1[n1 > 25])
# # n1[n1 < 30] = 0
# print(n1)

# count = 0
# for ele in n1:
#     if ele % 5 == 0:
#         count = count + 1
# print(count)

# task 6

# n1 = np.linspace(0,1,10)
# print(n1)

# n2 = np.eye(4)
# print(n2)

# n3 = np.random.randint(1,100,20)

# print(np.sort(n3))
# print(np.sort(n3)[-5])

# task 6
import time

a = np.random.random((100,100))
b = np.random.random((100,100))
start = time.time()

matrix = np.matmul(a,b)  # time taken 0.0021250247955322266
# print(matrix)

# det = np.linalg.det(matrix) # time taken 0.0012927055358886719
# print(det)

inverse = np.linalg.inv(matrix) # time taken 0.007465839385986328
print(inverse)

end = time.time()

print(end - start)





