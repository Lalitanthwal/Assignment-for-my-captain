#clear()
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
#copy()
car = {
  "brand": "Toyota",
  "model": "Avalon",
  "year": 1994
}

x = car.copy()

print(x)
#fromkeys()
x = ('key1', 'key2', 'key3')
y = 2

thisdict = dict.fromkeys(x, y)
#get()
laptop = {
  "brand": "Toshiba",
  "model": "Toshiba T1100",
  "year": 1985
}

x = laptop.get("model")

print(x)
#items()
car = {
  "brand": "Toyota",
  "model": "Avalon",
  "year": 1994
}

x = car.items()

print(x)
#keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)
#pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)
#popitem()
laptop = {
  "brand": "Toshiba",
  "model": "Toshiba T1100",
  "year": 1985
}
laptop.popitem()

print(laptop)
#setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

#update()
laptop = {
  "brand": "Toshiba",
  "model": "Toshiba T1100",
  "year": 1985
}
laptop.update({"color": "White"})

print(laptop)
#values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)







