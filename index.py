# name = "afzal"
# print(name)

# age = 20
# print(age)


# a = 10

# b = 10.4

# s = "Hello World"

# print(a)
# print(b)
# print(s)
# x = a+b;
# print("The sum of a and b is: ", x)

# is_true = False
# print(is_true)


# my_list = [1,2,3,4,5]
# print(my_list[0])

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])


# my_tuple = (1,2,3,4,5)
# print(my_tuple[0])
# print(my_tuple[1])
# print(len(my_tuple))

# dictionary = {
#   "name":"afzal",
#   "age":20,
# }


# a = 10
# b  = 20

# if(a>b):
#   print("a is greater than b")
# else:
#     print("b is greater than a")


# age = 20
# is_logged_in = False


# if(age > 18):
#   if(not is_logged_in):
#     print("you are an adult and not logged in")
#   else:
#     print("you are an adult and logged in")
# else:
#   print("You are a child")



# fruits = ["apple", "banana", "cherry"]


# # for x in fruits:
# #   print("the items in fruits are: \n", x)



# fruits = ["apple", "banana", "cherry"]

# # //print it backwards

# for fruit in fruits[::-1]:
#   print(fruit)



# count = 5

# while(count > 0):
#   print(count)
#   count -= 1


# def my_add_function(a,b):
#   return a+b

# def greet(name):
#   return "Hello " + name


# print(greet("afzal"))


def multiply(a,b,c):
  return a*b*c

print(multiply(2,3,4))


#write a function that takes a list of numbers and returns only the even ones
# def even_numbers(numbers):
#   even_numbers = []
#   for number in numbers:
#     if(number%2==0):
#       even_numbers.append(number)
#   return even_numbers
  
# print(even_numbers([1,2,3,4,5,6,7,8,9,10]))



# def even_numbers(nums):
#   even_nums = []
#   for num in nums:
#     if(num%2==0):
#       even_nums.append(num)
#   return even_nums
  


nums = [1,2,3,4,5,6,7,8,9,10]

even_nums = [num for num in nums if num % 2 == 0]