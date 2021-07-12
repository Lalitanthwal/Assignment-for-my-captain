#add()
thisset = {"pen", "pencil", "eraser"}

thisset.add("sharpner")

print(thisset)
#clear()
numbers = {"1", "2", "4"}

numbers.clear()

print(numbers)
#copy()
pens = {"reynolds", "pierre cardin", "parker"}

x = pens.copy()

print(x)
#difference()
x = {"4", "5", "2"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)
#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)
#discard()
thisset = {"pen", "pencil", "eraser"}

thisset.discard("eraser")

print(thisset)
#intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
#intersection_update()
x = {"eggs", "rice", "sandwitch"}
y = {"yahoo", "google", "bing"}

x.intersection_update(y)

print(x)
#isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)
#issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
#issuperset()
x = {"z", "y", "s","b", "a", "c" }
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)
#pop()
fruits = {"apple", "banana", "cherry"}

fruits.pop() 

print(fruits)
#remove()
numbers = {"1", "2", "3"}

numbers.remove("2")

print(numbers)
#symmetric_difference()
x = {"axe", "fogg", "set wet"}
y = {"playstation", "nintendo", "xbox"}

z = x.symmetric_difference(y)

print(z)
#symmetric_difference_update()
x = {"apple", "banana", "cherry"}
y = {"elephant", "dragon", "bear"}

x.symmetric_difference_update(y)

print(x)
#union()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)
#update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)
