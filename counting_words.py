text =""" Python data types have a static data type. That is, while defining a variable, no numerical, text or list definitions are made. Data types are divided into Primitive and Non-Primitive. Primitive data types are divided into 4 as int, float, string and boolean. Non-Primitive data types include List, Dictionary, Tuple, and Set.
"""

print(text.split())

word_count = {}

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

print("Enter a number: ")
user_num = input()
# user enters 10
print(user_num + user_num)

num1=float(input('1:'))
num2=float(input('2:'))
print(num1+num2)