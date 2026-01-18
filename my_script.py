print("Hello Jeep 2026")

a = 10
b = 20
c = a + b
print(c)

#List
l = [1, 2, 3, 4]
print(l)

print(l[0])

#Tuple
my_tuple = (1, "hello", 3.14)
print(my_tuple)
print(my_tuple[1])

#Dict
d = {
    "a" : 1,
    "b" : 2,
}
print(d)

# 2 method same as summary
print(d["a"])
print(d.get("a"))

#Set
my_set = set()
my_set.add(10)
my_set.add(10)

#loop | for
for i in range(11):
    print(i)

l = [1, 2, 3, 4]
for item in l:
    print(item)

d = {
    "a" : 1,
    "b" : 2
}
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")

#Classes and Object
class DataExtractor:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

data_extractor_object = DataExtractor(9)
print(data_extractor_object.get())

#Libraries Year . month . day
from datetime import datetime
now = datetime.now().strftime("%Y %m %d")
print(now)