from array import *
array1 = array('i', [10, 20, 30, 40])
array1.insert(1, 60)
array1.remove(40)

for x in array1:
    print(x)

print(array1.index(10))
