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


# def multiply(a,b,c):
#   return a*b*c

# print(multiply(2,3,4))


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
  
# s = "python"

# #reverse the string without built-in functions
# reverse_string = ""

# for i in range(len(s)-1,-1,-1):
#   reverse_string += s[i]

# print(reverse_string)

#write a function that takes a string and returns the reversed string
# def reverse_string(s):
#   reversed_string = ""
#   for i in range(len(s)-1,-1,-1):
#     reversed_string += s[i]
#   return reversed_string






# def function1(num):
#   if(num%2==0):
#     return "even"
#   else:
#     return "odd"

# print(function1(2))


# people = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35}
# ]


# for person in people:
#   print(person["name"], "is", person["age"], "years old")


#   5. Dictionary operations
# python# Given this dictionary, find and print the key with the highest value

# best_name = None
# best_score = -1
# scores = {"Alice": 85, "Bob": 92, "Charlie": 78}


# for name,score in scores.items():
#    if score > best_score:
#       best_name = name
#       best_score = score
    
# print(best_name, best_score)

# # print(max_key)

# class Car:
#    def __init__(self,brand,year):
#       self.brand = brand
#       self.year = year

#    def describe(self):
#       print(f"This {self.brand} car was made in {self.year}")


# my_car = Car("Toyota",2020)
# my_car.describe()


# def function1(sentence):
#    word = sentence.split()
#    return len(word)


# # print(function1("Hello World"))


# nums = [1,2,3,4,5,6,7,8,9,10]


# odd = [x for x in nums if x%2!=0]
# print(odd)

# labels = ["even" if x % 2 == 0 else "odd" for x in nums]
# print(labels)

# squares = {x:x**2 for x in range(1,6)}
# print(squares)


# words = ["python", "ai", "developer"]

# word_map = {word:len(word) for word in words}
# print(word_map)


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("That's not a valid number")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# else:
#     print(f"Result: {result}")   # runs if no exception
# finally:
#     print("Done")  


# try:
#    num = int(input("enter a num: "))
#    result = 10 * num
# except ValueError:
#    print("That's not a valid number")
# else:
#    print(f"Result: {result}")

# f = open("data.txt","r")
# content = f.read()
# f.close()


# with open("data.txt","r") as f:
#     content = f.read()
# #     print(content)
# with open("data.txt", "r") as f:
#     for line in f:            # iterate line by line (memory efficient)
#         print(line.strip())



# with open("output.txt", "w") as f:
#     f.write("Hello\n")
#     f.write("World\n")

# with open("output.txt", "a") as f:
#     f.write("New line\n")


try:
    with open("missing.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")