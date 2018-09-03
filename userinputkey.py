dict={1:'sanjana',2:'pratiksha'}
user=int(input('Enter the key:'))
dict1=user
print(dict)
if dict1 in dict:
    print ("key is there")
    del dict[dict1]
    print(dict)
else:
    print("key not present")
-------------------------------------------------------------------------------
-----------------------------------------------------------------------------
