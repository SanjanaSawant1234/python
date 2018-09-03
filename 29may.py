Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> • Write a Python program to remove an item from a tuple.
SyntaxError: invalid character in identifier
>>> mu_tuple=(1,2,3,4,5)
>>> del mu_tuple[3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    del mu_tuple[3]
TypeError: 'tuple' object doesn't support item deletion
>>> del mu_tuple([0])
SyntaxError: can't delete function call
>>> ###
>>> tuple=(1,2,3,4,5)
>>> tuple.index(3)
2
>>> ###
>>> tuple=(1:'sanjana',2:19)
SyntaxError: invalid syntax
>>> tuple(dict)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(dict)
TypeError: 'tuple' object is not callable
>>> ###
>>> tuple(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tuple(1,2,3,4)
TypeError: 'tuple' object is not callable
>>> tuple=(1,2,3,4)
>>> list=tuple()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list=tuple()
TypeError: 'tuple' object is not callable
>>> list(tuple)
[1, 2, 3, 4]
>>> list(tuple(0,1,2,3))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(tuple(0,1,2,3))
TypeError: 'tuple' object is not callable
>>> list(tuple[0])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(tuple[0])
TypeError: 'int' object is not iterable
>>> list(tuple(0))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(tuple(0))
TypeError: 'tuple' object is not callable
>>> list[0]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list[0]
TypeError: 'type' object is not subscriptable
>>> list[tupl[0]]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list[tupl[0]]
NameError: name 'tupl' is not defined
>>> list.pop[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list.pop[0]
TypeError: 'method_descriptor' object is not subscriptable
>>> type(tuple)
<class 'tuple'>
>>> tuple.pop(0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple.pop(0)
AttributeError: 'tuple' object has no attribute 'pop'
>>> 
>>> tuple.pop[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple.pop[0]
AttributeError: 'tuple' object has no attribute 'pop'
>>> list(tuple[0])
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list(tuple[0])
TypeError: 'int' object is not iterable
>>> list
<class 'list'>
>>> tuple=(1,2,3,4,5)
>>> list(tuple)
[1, 2, 3, 4, 5]
>>> list=(tuple)
>>> list
(1, 2, 3, 4, 5)
>>> tuple=(list)
>>> tuple
(1, 2, 3, 4, 5)
>>> list
(1, 2, 3, 4, 5)
>>> tuple.pop[0]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    tuple.pop[0]
AttributeError: 'tuple' object has no attribute 'pop'
>>> del tuple[0]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del tuple[0]
TypeError: 'tuple' object doesn't support item deletion
>>> list=(1,2,3,4)
>>> list
(1, 2, 3, 4)
>>> list(tuple.index[0])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(tuple.index[0])
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> tuple
(1, 2, 3, 4, 5)
>>> tuple[-5:]
(1, 2, 3, 4, 5)
>>> tuple[:-5]
()
>>> tuple[-1:-5]
()
>>> tuple[-5:-1]
(1, 2, 3, 4)
>>> tuple.reverse()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tuple.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
>>> for i in tuple(list(tuple).index[0])
SyntaxError: invalid syntax
>>> for i in tuple(list(tuple).index[0]:)
SyntaxError: invalid syntax
>>> for i in tuple(list(tuple).index[0]):
	print(tuple)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for i in tuple(list(tuple).index[0]):
TypeError: 'tuple' object is not callable
>>>  Write a Python script to concatenate following dictionaries to create a new one. Sample Dictionary :  dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
SyntaxError: unexpected indent
>>> dict1={1:10,2:20}
>>> dict2={3:30,4:40}
>>> dict3={5:50,6:60}
>>> dict1.update(dict2)
>>> dict1
{1: 10, 2: 20, 3: 30, 4: 40}
>>> dict1.update(dict3)
>>> dict1
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
>>> ###
>>> del dict1[0]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    del dict1[0]
KeyError: 0
>>> dict1.pop(1,none)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict1.pop(1,none)
NameError: name 'none' is not defined
>>> del dict1[0]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    del dict1[0]
KeyError: 0
>>> del dict1[2]
>>> dict1
{1: 10, 3: 30, 4: 40, 5: 50, 6: 60}
>>> for i in dict1():
	print(dict1)

	
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    for i in dict1():
TypeError: 'dict' object is not callable
>>> for i in dict1():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    for i in dict1():
TypeError: 'dict' object is not callable
>>> 
>>> dict1={1:'gh',2:'ggr'}

>>> for i in dict1():
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    for i in dict1():
TypeError: 'dict' object is not callable
>>> for key in dict1():
	print(key)

	
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    for key in dict1():
TypeError: 'dict' object is not callable
>>> for key in dict1:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#81>", line 2, in <module>
    print(i)
NameError: name 'i' is not defined
>>> for key in dict1:
	print(key)

	
1
2
>>> for key in dict1.items():
	print(key)

	
(1, 'gh')
(2, 'ggr')
>>> • Print the numbers in the range 33 to 49 (inclusive).
SyntaxError: invalid character in identifier
>>> ###
>>> for i in range(33,49):
	print(i)

	
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
>>> tuple=(1,2,3)
>>> tuple[3]=4
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    tuple[3]=4
TypeError: 'tuple' object does not support item assignment
>>> tuple.update(4)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tuple.update(4)
AttributeError: 'tuple' object has no attribute 'update'
>>> tuple.insert(4)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    tuple.insert(4)
AttributeError: 'tuple' object has no attribute 'insert'
>>> for i iin range(10,1):
	
SyntaxError: invalid syntax
>>> tuple=(1,2,3,4,5,6)
>>> l1=list(tuple)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    l1=list(tuple)
TypeError: 'tuple' object is not callable
>>> list(tuple)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    list(tuple)
TypeError: 'tuple' object is not callable
>>> list=(tuple)
>>> list
(1, 2, 3, 4, 5, 6)
>>> list(tuple)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    list(tuple)
TypeError: 'tuple' object is not callable
>>> temps=[25.2,16.8,31.4,23.9,28,22.5,19.6]
>>> temps
[25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> temps.sort()
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> tuple=(1,2,3,4,5)
>>> list(tuple)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    list(tuple)
TypeError: 'tuple' object is not callable
>>> l1=list(tuple)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    l1=list(tuple)
TypeError: 'tuple' object is not callable
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
(2, 3, 4, 5)
>>> 
====================== RESTART: C:/Users/sanjana/tup.py ======================
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[5, 4, 3, 2]
(5, 4, 3, 2)
>>> 
===================== RESTART: E:/sanjana/tupletodict.py =====================
{'w': 2, 'r': 3}
>>> l1=['s','a','n','j','a','n','a']
>>> for i in l1:
	print(i)

	
s
a
n
j
a
n
a
>>> for i in l1:
	print(i,end='')

	
sanjana
>>> l1.format()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    l1.format()
AttributeError: 'list' object has no attribute 'format'
>>> l1.join()
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    l1.join()
AttributeError: 'list' object has no attribute 'join'
>>> join(l1)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    join(l1)
NameError: name 'join' is not defined
>>> ''.join(11)
'sanjana'
>>> ###
>>> 
===================== RESTART: E:/sanjana/dict update.py =====================
{'a': 100, 'b': 200, 'x': 300, 'y': 200}
>>> 
========================= RESTART: E:/sanjana/zip.py =========================
[(1, 3, 5), (2, 4, 6)]
>>> 
========================= RESTART: E:/sanjana/zip.py =========================
[((1, 2),), ((3, 4),), ((5, 6),)]
>>> tup=(1,2,1,3,4)
>>> tup.count(1)
2
>>> print[33:49]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print[33:49]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print([33:49])
SyntaxError: invalid syntax
>>> range[33:49]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    range[33:49]
TypeError: 'type' object is not subscriptable
>>> int[33:49]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    int[33:49]
TypeError: 'type' object is not subscriptable
>>> 
