print("Initial dictionary")
dict={'c':3,'a':1,'b':2,'d':4}
print(dict)
d=input("Enter the key to delete:")
if d in dict:
    del dict[d]
    print("updated dictionary")
    print(dict)
else:
    print("key not found")
