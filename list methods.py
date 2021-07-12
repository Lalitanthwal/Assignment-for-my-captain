# append()
thislist=["apple","banana","cherry"]
thislist.append("cherry")
print(thislist)
#del[:]
mylist=["computer","Playstation","desktop"]
del thislist[:]
print('Thislist:',thislist)
#copy()
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
#count()
fruits = ['guava', 'melon', 'plum']
x = fruits.count('plum')
print(x)
#extend()
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
#index()
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
#insert()
cars = ['mercedes', 'hyundai', 'toyota']

cars.insert(1, "jaguar")

print(cars)
#pop()
pens = ['luxor', 'parkar', 'pierre cardin']

pens.pop(1)

print(pens)
#remove()
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
#reverse()
candies = ['candyman', 'mentos', 'londonderry']

candies.reverse()

print(candies)
#sort()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)
