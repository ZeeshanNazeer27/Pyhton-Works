# def greet_user():
#     print("Hello,User")
# greet_user()

# def greeting(name):
#     print(f"Hello , {name}")

# name = "Ali"
# greeting(name)

# def greeting(name = "Zeeshan"):
#     print(f"Hello , {name}")

# greeting("Ali")

# Return
# def square(number):
#     sq = number * number
#     return sq

# num = int(input("Enter the value : "))
# result = square(num)
# print("Result is : ",result)

#Recursion
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num -1)
    
# print(factorial(5))

#lambda
# x = lambda num : num /2
# print(x(4))

# x = lambda a,b : a*b
# print(x(3,4))
area_circle_lambda = lambda r: 3.14159 * r ** 2
print(area_circle_lambda(3))

def count_vowels(text) :
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
print(count_vowels("Hello world"))

def sum_list(numbers):
    return sum(numbers)
print(sum_list([1,2,4]))


def dict_keys(d: dict) -> list:
    return list(d.keys())
print(dict_keys({"a":1,"b":2}))

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(37))

exists_in_set_lambda = lambda s, val: val in s
print(exists_in_set_lambda(("abc"),"f"))