

from array import array

arr = array('i', [10,20,30,40,50])

# Accessing array elements
print("Accessing array elements")
print (arr[0])
print (arr[2])
print("-" * 20)

# insert()
print("Inserting 60 at index 1.....")
arr.insert(1,60)

# remove()
arr.remove(40)
print("-" * 20)

# Search
try:
    print(arr.index(40))
except:
    print("Value not found")
print("-" * 20)

# Updating
print("Updating index 2 equal to 80")
arr[2] = 80

print("-" * 20)
for x in arr:
     print(x)