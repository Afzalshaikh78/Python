import numpy as np
# # arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr = np.arange(1,21)
# print(arr)


# matrix = arr.reshape(4,5)
# print(matrix)

# second_row = matrix[1]
# last_column = matrix[:,-1]

# doubled = matrix*2
# total = doubled.sum()


# print(total)


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

element_wise_sum = arr + arr2
print(element_wise_sum)

element_wise_product = arr * arr2
print(element_wise_product)

element_wise_difference = arr - arr2
print(element_wise_difference)


element_wise_product2 = arr @ arr2
print(element_wise_product2)