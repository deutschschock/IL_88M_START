#for
fruits2 = ["apple", "banana", "cherry"]
for fruit in fruits2:
    print(fruit)

for i in range(5):
    print(i)

for i in range(1,10,2):
    print(i)

#while
count = 1
while count < 5:
    print(count)
    count += 1

#function
def add(a,b):
    return a+b
def is_even(a):
    return a % 2 == 0

def  min_max(numbers):
    return min(numbers),max(numbers)

low, high = min_max(range(3,401,55))
print(low,high)

def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
print(sum_list([4,2,0,0,1,2,-5]))

def count_vowels(text):
    #vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in text.lower():
        if char in 'aeiou':
            count += 1
    return count

#exception
input_str = 'wrwe'

try:
    number = int(input_str)
    print(number)
except ValueError:
    print(ValueError)

def divide(a,b) :
    try:
        return a/b
    except ZeroDivisionError:
        print(ZeroDivisionError)
        return 0
    except TypeError:
        print(TypeError)
        return 0

print(divide(3,4))
print(divide(3,0))
print(divide('ssfs',1))

try:

    print("try")
    numbers = [1,2,3]
    print(numbers[3])
except (IndexError, TypeError) as e:
    print("except")
    print(e.__class__)
else:
    print("else")
    print(type(numbers))
finally:
    print("finally")









