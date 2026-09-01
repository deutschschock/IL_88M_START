fruits = ["яблоко","банан","груша"]
numbers = [0,1,2,3,4,5,6,7,8,9]
mix = ["text",55,12.5,True]
empty = []

print(type(empty))
print(fruits[1])
print(fruits[::-1])
print(fruits[-1])

fruits[1] = 'orange'
print(fruits[::-1])
fruits.append('lemon')
print(fruits)

fruits.insert(1,'kiwi')
print(fruits)
fruits.remove('kiwi')
print(fruits)

last = fruits.pop()
print(last)
print(fruits)

numbers2 = [99,1,2,34,4,5,6,78,8,9]
print(sorted(numbers2))
print(sorted(numbers2,reverse=True))
print(min(numbers2),max(numbers2),sum(numbers2))
print("is 34 in numbers2", 34 in numbers2)

numbers2.sort()
print(numbers2)
for number in numbers2:
    print(number)

for fruit in fruits:
    print(fruit)

#tuple
fruits.sort()
print(fruits)
coordinates1= (10,20)
print(type(coordinates1))
single = (34)
print(type(single))

tuple1 = 1,2,3
print(type(tuple1))

print(coordinates1[0])
print(coordinates1[-1])

x,y = coordinates1
print(x,y)

#dict

person = {
    "name": "Alex",
    "age":45,
    "city":"Backnang"
}
print(person)

print("length of person", len(person))
print(person["name"])

print(person.get("age"))
print(person.get("email"))
print(person.get("email","not found"))

person["email"] = "alex@welt.my"
person["age"] = 41
print(person)

del person["city"]
print(person)

print("name" in person)

dict_any = {
    1: "1",
    "two":2,
    (0,1): "three"
}
print(dict_any)
dict_any[(True, False)] = True
print(dict_any)
dict_any[( False, True)] = False
print(dict_any)
print((True, False) == (1,0))

prices = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
}
for product in prices:
    print("product",product)

print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))

#set
colors ={"red","green","blue"}
print(colors)
colors.discard("red")
print(colors)
print("red" in colors)
print("green" in colors)

numbers_set = {1,2,3,4,5,6,6,8,7,8,9}
print(numbers_set)

empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 - set2)
print(set2 - set1)
print(set1 & set2)
print(set1 | set2)
