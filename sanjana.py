Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> to_do="LEARN PYTHON"
>>> print(to_do)
LEARN PYTHON
>>> print(to_do[0])
L
>>> print(to_do[6:11])
PYTHO
>>> a="QWERTY"
>>> print(a[5:6:3:4])
SyntaxError: invalid syntax
>>> print(a[5:6])
Y
>>> print(a[4:5])
T
>>> print(a[4:6])
TY
>>> print(a[4:6]a[2:4])
SyntaxError: invalid syntax
>>> print(a[4:6])
TY
>>> print(a[2:4])
ER
>>> print(a[4:6],[2:4])
SyntaxError: invalid syntax
>>> print(a[4:6],a[2:4])
TY ER
>>> grocery_list=['tomatoes','brocoli','mushrooms','beetroot']
>>> user_details=['chitvan',25,'a_ve']
>>> print(grocery_list[1])
brocoli
>>> print(user_details*2)
['chitvan', 25, 'a_ve', 'chitvan', 25, 'a_ve']
>>> print(grocery_list[1:3])
['brocoli', 'mushrooms']
>>> grocery_list[:]
['tomatoes', 'brocoli', 'mushrooms', 'beetroot']
>>> pytuple=('Angela','Hilary','kiran',2017)
>>> pytuple
('Angela', 'Hilary', 'kiran', 2017)
>>> pytuple[0]
'Angela'
>>> pytuple[0:3]
('Angela', 'Hilary', 'kiran')
>>> pytuple*2
('Angela', 'Hilary', 'kiran', 2017, 'Angela', 'Hilary', 'kiran', 2017)
>>> pytuple+pytuple
('Angela', 'Hilary', 'kiran', 2017, 'Angela', 'Hilary', 'kiran', 2017)
>>> pytuple[:]
('Angela', 'Hilary', 'kiran', 2017)
>>> pytuple[2:]
('kiran', 2017)
>>> my_tuple=('sanjana',12,34,'pratiksha')
>>> my_tuple[0:2]
('sanjana', 12)
>>> my_tuple[0::2]
('sanjana', 34)
>>> dict{}
SyntaxError: invalid syntax
>>> dict={}
>>> dict['Apple']="A fruit,red in color"
>>> dict['Appoint']="to call upon"
>>> dict2={'Name':'sanjana','code-name':'citizenfour','emp-id':1234,'os':'linux'}
>>> dict2
{'Name': 'sanjana', 'code-name': 'citizenfour', 'emp-id': 1234, 'os': 'linux'}
>>> dict
{'Apple': 'A fruit,red in color', 'Appoint': 'to call upon'}
>>> dict.keys()
dict_keys(['Apple', 'Appoint'])
>>> dict.values()
dict_values(['A fruit,red in color', 'to call upon'])
>>> dict2.keys()
dict_keys(['Name', 'code-name', 'emp-id', 'os'])
>>> dict2.values()
dict_values(['sanjana', 'citizenfour', 1234, 'linux'])
>>> b=2
>>> a=3
>>> b**=a
>>> b
8
######>>> b//=a
>>> b

2
>>> b/=a
>>> b
0.6666666666666666
>>> b%=a
>>> b
0.6666666666666666
>>> b/a
0.2222222222222222
>>> b=b/a
>>> b
0.2222222222222222
##############
>>> a=b=c=1
>>> a,b,c=1,2,'sum='
>>> print(c,a+b)
sum= 3
>>> a=10
>>> b=13
>>> print("ANDing:",a,"&b:",b,"is",a&b,":"bin(a&b))
SyntaxError: invalid syntax
>>> print("ANDing a:",a,"&b:",b,"is",a&b,":",bin(a&b))
ANDing a: 10 &b: 13 is 8 : 0b1000
>>> *
SyntaxError: invalid syntax
>>> a=[1,2,3,4,5],x=2,y=7
SyntaxError: can't assign to literal
>>> a=[1,2,3,4,5];x=2,y=7
SyntaxError: can't assign to literal
>>> a=[1,2,3,4,5];x=2;y=7
>>> x-y in a
False
>>> y-x in a
True
>>> y not in a
True



>>> 

Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s1='sanjana'
>>> print("Update String:",s1[:6]+'sir')
Update String: sanjansir
>>> print("update String:",s1[:8]+'mam')
update String: sanjanamam
>>> s1
'sanjana'
>>> s1[:8]+'  mam'
'sanjana  mam'
>>> s1=''MITTU'
SyntaxError: invalid syntax
>>> S1='MITTU'
>>> print(s1+ '\b' + 'SKILLOLOGIES')
sanjanaSKILLOLOGIES
>>> print(s1+  '\b'  +'sillologies')'
SyntaxError: EOL while scanning string literal
>>> print(s1+   '\b'  +'skillologies')
sanjanaskillologies
>>> print(S1 +  '\b'   +'skillologies')
MITTUskillologies
>>> R"\tHello"
'\\tHello'
>>> r"\tHello"
'\\tHello'
>>> a="Mitu"
>>> b="Skillologies"
>>> print("concatination:\t\t",a+b)
concatination:		 MituSkillologies
>>> print("Repetetion:\t\t", a*3)
Repetetion:		 MituMituMitu
>>> print("slice:\t", a[1])
slice:	 i
>>> print("Range slice:\t",b[3:9])
Range slice:	 llolog
>>> print("H in string var:",'H'in a)
H in string var: False
>>> print("i not in string var:\t",'m'not in a)
i not in string var:	 True
>>> print("R/r for raw string:\t"R"\tHello")
R/r for raw string:	\tHello
>>> *
SyntaxError: invalid syntax
>>> name="dyanESHWARI"
>>> print("name.capitalize() :",name.capitalize())
name.capitalize() : Dyaneshwari
>>> name="dyanESHWARI"
>>> print("name.center(30,'_'):",name.center(30,'_'))
name.center(30,'_'): _________dyanESHWARI__________
>>> name=dyanESHWARI
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    name=dyanESHWARI
NameError: name 'dyanESHWARI' is not defined
>>> name="dyanESHWARI"
>>> print("name.count('A'):",name.count('A'))
name.count('A'): 1
>>> print("\n","starts with".center(40,'~'))

 ~~~~~~~~~~~~~~starts with~~~~~~~~~~~~~~~
>>> print("String:"stri,"\nstarts with:This in 0-3",stri.startswith('This',0,3))
SyntaxError: invalid syntax
>>> stri="This is some string for testing"
>>> print("string:"stri,"\nstarts with:This in 0-3",stri.startswith('This',0,3))
SyntaxError: invalid syntax
>>> 
>>> stri="This is some string for testing"
>>> print("String:",stri,"\nStarts with:This in 0_3",stri.startswith('This',0,3))
String: This is some string for testing 
Starts with:This in 0_3 False
>>> name="dyanESHWARI"
>>> print("\n","ENDSWITH".center(40,'~'))

 ~~~~~~~~~~~~~~~~ENDSWITH~~~~~~~~~~~~~~~~
>>> print("name.endwith('RI')\t\t",name.endswith('RI'))
name.endwith('RI')		 True
>>> print("name.endswith('A',2,6)",name.endswith('A',2,6))
name.endswith('A',2,6) False
>>> print("\n","ENDSWITH".center(40,'~'))

 ~~~~~~~~~~~~~~~~ENDSWITH~~~~~~~~~~~~~~~~
>>> print("\n", "INDEXING".center(40,'~'))

 ~~~~~~~~~~~~~~~~INDEXING~~~~~~~~~~~~~~~~
>>> name2="Rubber baby buggy bumper"
>>> print(name2.index("Rubber"))
0
>>> print(name2.index("bumper",15))
18
>>> print(name2.index("bumper",18,20))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(name2.index("bumper",18,20))
ValueError: substring not found
>>> print("1. CE1G2P017", "CE1G2P017".isalnum())
1. CE1G2P017 True
>>> print("\n.ALPHA-BETA","ALPHA-BETA".isalpha())

.ALPHA-BETA False
>>> print("\n11254".isnumeric())
False
>>> print("\n11254","11254".isnumeric())

11254 True
>>> print("\n","IS DIGIT".center(40,'~'))

 ~~~~~~~~~~~~~~~~IS DIGIT~~~~~~~~~~~~~~~~
>>> print("125463","125463".isdigit())
125463 True
>>> print("1254a1".isdigit())
False
>>> print("\n","JOIN".center(40,'~'))

 ~~~~~~~~~~~~~~~~~~JOIN~~~~~~~~~~~~~~~~~~
>>> sequence=("Apple","Mango","strawberry")
>>> sep=","
>>> print(sequence,"is now written with  seperator as:",sep.join(sequence))
('Apple', 'Mango', 'strawberry') is now written with  seperator as: Apple,Mango,strawberry
>>> name2="Rubber baby buggy bumper"
>>> print("\n","CALL LENGTH".center(40,'~'))

 ~~~~~~~~~~~~~~CALL LENGTH~~~~~~~~~~~~~~~
>>> print("size of",name2,"is",len(name2))
size of Rubber baby buggy bumper is 24
>>> print("\n","SWAPCASE".center(40,'~'))

 ~~~~~~~~~~~~~~~~SWAPCASE~~~~~~~~~~~~~~~~
>>> string1="This is good example to show!"
>>> print("Actual string >",string1,"\n",string1.swapcase())
Actual string > This is good example to show! 
 tHIS IS GOOD EXAMPLE TO SHOW!
>>> 
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l1=[4353,2314,2956,9362,3900]
>>> l1.remove(2956)
>>> l1
[4353, 2314, 9362, 3900]
>>> l1.getindex(9962)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l1.getindex(9962)
AttributeError: 'list' object has no attribute 'getindex'
>>> l1.index(9962)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l1.index(9962)
ValueError: 9962 is not in list
>>> l1.getIndex(9962)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l1.getIndex(9962)
AttributeError: 'list' object has no attribute 'getIndex'
>>> l1.index[9962]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l1.index[9962]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l1.index(9962)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l1.index(9962)
ValueError: 9962 is not in list
>>> l1.insert(3,4499)
>>> l1
[4353, 2314, 9362, 4499, 3900]
>>> del l1[1]
>>> l1
[4353, 9362, 4499, 3900]
>>> l1.extend(5,5566,1830)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l1.extend(5,5566,1830)
TypeError: extend() takes exactly one argument (3 given)
>>> l1.extend(5566,1830)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l1.extend(5566,1830)
TypeError: extend() takes exactly one argument (2 given)
>>> l1.extend(5566)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l1.extend(5566)
TypeError: 'int' object is not iterable
>>> l1.extend([5566,1830])
>>> l1
[4353, 9362, 4499, 3900, 5566, 1830]
>>> l1.extend[5]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l1.extend[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> l1.extend([66])
>>> l1
[4353, 9362, 4499, 3900, 5566, 1830, 66]
>>> 11.sort()
SyntaxError: invalid syntax
>>> l1.reverse()
>>> l1
[66, 1830, 5566, 3900, 4499, 9362, 4353]
>>> sort(l1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sort(l1)
NameError: name 'sort' is not defined
>>> l1.sort()
>>> l1
[66, 1830, 3900, 4353, 4499, 5566, 9362]
>>> l1=['physics','chemistry',1997,2000]
>>> print("vat")
vat
>>> print(l1[2])
1997
>>> print("new value available at index 2")
new value available at index 2
>>> print(l1[2])
1997
>>> w=input("enter value:")
enter value:34
>>> print(l1[2])
1997
>>> l1.insert(1,2001)
>>> l1
['physics', 2001, 'chemistry', 1997, 2000]
>>> print(l1[2])
chemistry
>>> l1.insert(2,2003)
>>> l1
['physics', 2001, 2003, 'chemistry', 1997, 2000]
>>> l1[2]
2003
>>> l1.Index(2003)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    l1.Index(2003)
AttributeError: 'list' object has no attribute 'Index'
>>> l1.index([2003])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l1.index([2003])
ValueError: [2003] is not in list
>>> index(l1[2003])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    index(l1[2003])
NameError: name 'index' is not defined
>>> l1.index(2003)
2
>>> l1 [2]='sanjana'
>>> l1
['physics', 2001, 'sanjana', 'chemistry', 1997, 2000]
>>> len([1,2,3])
3
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> ['HI']*4
['HI', 'HI', 'HI', 'HI']
>>> 3 in [1,2,3]
True
>>> for x in [1,2,3];x
SyntaxError: invalid syntax
>>> for x in [1,2,3]
SyntaxError: invalid syntax
>>> For x in [1,2,3]
SyntaxError: invalid syntax
>>> For X in [1,2,3]
SyntaxError: invalid syntax
>>> For x in [1,2,3]:print(x)
SyntaxError: invalid syntax
>>> for x in [1,2,3]:
	print(x)

	
1
2
3
>>> colors=['yellow','red','blue','green','black']
>>> colors[1:3]
['red', 'blue']
>>> colors[0:]
['yellow', 'red', 'blue', 'green', 'black']
>>> colors[:4]
['yellow', 'red', 'blue', 'green']
>>> colors[:]
['yellow', 'red', 'blue', 'green', 'black']
>>> colors[-1]
'black'
>>> colors[-1:]
['black']
>>> colors[-1:-5]
[]
>>> colors[-5]
'yellow'
>>> l2=['9:00','10:30','14:00','15:00','15:30']
>>> l2
['9:00', '10:30', '14:00', '15:00', '15:30']
>>> l2.append('16:30')
>>> l2
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> l2+['16:30']
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '16:30']
>>> l2+['17:30','18:30']
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '17:30', '18:30']
>>> l3=[25.2,16.8,31.4,23.9,28,22.5,19.6]
>>> l3
[25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> l3.sort()
>>> l3
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> cool_temp(l3[0:2])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    cool_temp(l3[0:2])
NameError: name 'cool_temp' is not defined
>>> l3[0:2]
[16.8, 19.6]
>>> l3[2:7]
[22.5, 23.9, 25.2, 28, 31.4]
>>> l=['physics','Physics','PHYSICS']
>>> l
['physics', 'Physics', 'PHYSICS']
>>> l[-2:]
['Physics', 'PHYSICS']
>>> l,l1=[123,'xyz'],[456,'abc']
>>> print cmp(l,l1)
SyntaxError: invalid syntax
>>> max(l)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    max(l)
TypeError: '>' not supported between instances of 'str' and 'int'
>>> l4=[1,2,3,4]
>>> l4
[1, 2, 3, 4]
>>> max(l4)
4
>>> l==l2
False
>>> function()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    function()
NameError: name 'function' is not defined
>>> cmp([l,l1])
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    cmp([l,l1])
NameError: name 'cmp' is not defined
>>> module
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    module
NameError: name 'module' is not defined
>>> l.compare(l1)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    l.compare(l1)
AttributeError: 'list' object has no attribute 'compare'
>>> l.cmp(l1)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l.cmp(l1)
AttributeError: 'list' object has no attribute 'cmp'
>>> l.cmp([l1])
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    l.cmp([l1])
AttributeError: 'list' object has no attribute 'cmp'
>>> l5=[123,'xyz','zara','abc',123]
>>> l5
[123, 'xyz', 'zara', 'abc', 123]
>>> l5.count(123)
2
>>> l5.pop(abc)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    l5.pop(abc)
NameError: name 'abc' is not defined
>>> l5.pop()
123
>>> l5.pop(2)
'zara'
>>> l5.pop()
'abc'
>>> l5.push('sanjana')
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    l5.push('sanjana')
AttributeError: 'list' object has no attribute 'push'
>>> 
Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pytup0=("Hello",99.3j)
>>> pytup1=("world",2.4j)
>>> pytup0[0]=("python")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pytup0[0]=("python")
TypeError: 'tuple' object does not support item assignment
>>> tup2=(1,2,3,4,5,6,7)
>>> del tup2
>>> tup2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tup2
NameError: name 'tup2' is not defined
>>> tuple=(1)
>>> tuple
1
>>> tuple=tuple(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tuple=tuple(1)
TypeError: 'int' object is not callable
>>> tuple=1,2,3,4,5
>>> tuple
(1, 2, 3, 4, 5)
>>> tuple=1
>>> tuple
1
>>> type(tuple(1))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(tuple(1))
TypeError: 'int' object is not callable
>>> type(1)
<class 'int'>
>>> type((1))
<class 'int'>
>>> (1)
1
>>> tup(1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tup(1)
NameError: name 'tup' is not defined
>>> tuple=(1,2)
>>> tuple
(1, 2)
>>> tuple=()
>>> t1=2
>>> tuple
()
>>> type(tuple(1))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    type(tuple(1))
TypeError: 'tuple' object is not callable
>>> ###
>>> tup=('abc',)
>>> typle(tup)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    typle(tup)
NameError: name 'typle' is not defined
>>> type(tup)
<class 'tuple'>
>>> ###
>>> kingdom=['Bacteria','Protozoa','Chromista','Plantea','Fungi','Animalia']
>>> kingdom[0]
'Bacteria'
>>> kingdom[5]
'Animalia'
>>> kingdom[0:3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdom[2:5]
['Chromista', 'Plantea', 'Fungi']
>>> kingdom[4:6]
['Fungi', 'Animalia']
>>> kingdom[]
SyntaxError: invalid syntax
>>> kingdom[6]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    kingdom[6]
IndexError: list index out of range
>>> kingdom(:)
SyntaxError: invalid syntax
>>> kingdom[:]
['Bacteria', 'Protozoa', 'Chromista', 'Plantea', 'Fungi', 'Animalia']
>>> kingdom[]
SyntaxError: invalid syntax
>>> kingdom[-1]
'Animalia'
>>> kingdom[-1:-2]
[]
>>> kingdom[-1:-1]
[]
>>> kingdom[-3:-1]
['Plantea', 'Fungi']
>>> kingdom[-1:-4]
[]
>>> kingdom[-2:]
['Fungi', 'Animalia']
>>> kingdom[-1:-2]
[]
>>> kingdom[-2:-1]
['Fungi']
>>> contact={"first":"john","last":"doe","age":39,"sex":"male","salary":70000,"registered":"true"}
>>> contact.keys()
dict_keys(['first', 'last', 'age', 'sex', 'salary', 'registered'])
>>> contact.values()
dict_values(['john', 'doe', 39, 'male', 70000, 'true'])
>>> contact['salary']=90000
>>> contact
{'first': 'john', 'last': 'doe', 'age': 39, 'sex': 'male', 'salary': 90000, 'registered': 'true'}
>>> del contact['last']
>>> 
>>> contact
{'first': 'john', 'age': 39, 'sex': 'male', 'salary': 90000, 'registered': 'true'}
>>> contact['mob']=9702101004
>>> contact
{'first': 'john', 'age': 39, 'sex': 'male', 'salary': 90000, 'registered': 'true', 'mob': 9702101004}
>>> 
>>> for key in contact:
	print(key)

	
first
age
sex
salary
registered
mob
>>> for key in contact.iterkeys():
	print(key)

	
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for key in contact.iterkeys():
AttributeError: 'dict' object has no attribute 'iterkeys'
>>> for key in contact.keys
SyntaxError: invalid syntax
>>> for key in contact.keys():
	print(key)

	
first
age
sex
salary
registered
mob
>>> contact.copy()
{'first': 'john', 'age': 39, 'sex': 'male', 'salary': 90000, 'registered': 'true', 'mob': 9702101004}
>>> contact.fromkeys(seq)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    contact.fromkeys(seq)
NameError: name 'seq' is not defined
>>> contact.get(key)
9702101004
>>> contact.has_key(key)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    contact.has_key(key)
AttributeError: 'dict' object has no attribute 'has_key'
>>> contact.has_key('mob')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    contact.has_key('mob')
AttributeError: 'dict' object has no attribute 'has_key'
>>> dict={'seq':'value'}
>>> dict.fromkeys(seq)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    dict.fromkeys(seq)
NameError: name 'seq' is not defined
>>> dict.fromkeys(key)
{'m': None, 'o': None, 'b': None}
>>> dict.clear()
>>> 
>>> dict
{}
>>> 
