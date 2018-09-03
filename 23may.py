Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ###
>>> x=6
>>> x
6
>>> print(6)
6
>>> print("6")
6
>>> print(x)
6
>>> ###
>>> x=7
>>> x
7
>>> print(x)
7
>>> print("x")
x
>>> ###
>>> 10=x
SyntaxError: can't assign to literal
>>> x=10
>>> x
10
>>> ###
>>> x,y,z=1,2,3
>>> x
1
>>> y
2
>>> z
3
>>> ###
>>> 'n'
'n'
>>> '\n'
'\n'
>>> x=2
>>> y=3
>>> c=x+y
>>> print("sum is\n"c)
SyntaxError: invalid syntax
>>> print("sum is\n",c)
sum is
 5
>>> ###
>>> print("A\nB\nC\nD\nE\nF\n")
A
B
C
D
E
F

>>> ###
>>> x=2
>>> print("x")
x
>>> print('x')
x
>>> print(x)
2
>>> print("x+1")
x+1
>>> print('x'+1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('x'+1)
TypeError: must be str, not int
>>> print(x+1)
3
>>> ###
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:3
>>> print("circumference is",c)
circumference is 0.0
>>> eval("x+1")
3
>>> eval("x")
2
>>> r=float(input("Enter the radius"))
Enter the radius3.2
>>> print("circumference is",c)
circumference is 0.0
>>> c.py
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.py
AttributeError: 'float' object has no attribute 'py'
>>> E:/sanjana/c.py
SyntaxError: invalid syntax
>>> E:\sanjana\c.py
SyntaxError: unexpected character after line continuation character
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:2.3
>>> 
KeyboardInterrupt
>>> print("circumference is",c)
circumference is 20.096000000000004
>>> 2*3.14*2.3
14.443999999999999
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 14.443999999999999
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 0.0
>>> r=1
>>> PI=3.14
>>> c=2*PI*r
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>>  print("circumference is",c)
 
SyntaxError: unexpected indent
>>> print("circumference is",c)
circumference is 6.28
>>> ###
>>> a=0
>>> while(a<100):
	print("*",end=")
	      
SyntaxError: EOL while scanning string literal
>>>  while(a<100):
	print("*",end=");
	      
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:3
circumference is 12.56
>>> 2*3.14*3
18.84
>>> 2*3.14*1
6.28
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
2.3
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: could not convert string to float: 
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2.3
circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print("*",end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print('*',end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 4
    a+=1
    ^
IndentationError: unexpected indent
>>> Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ###
>>> x=6
>>> x
6
>>> print(6)
6
>>> print("6")
6
>>> print(x)
6
>>> ###
>>> x=7
>>> x
7
>>> print(x)
7
>>> print("x")
x
>>> ###
>>> 10=x
SyntaxError: can't assign to literal
>>> x=10
>>> x
10
>>> ###
>>> x,y,z=1,2,3
>>> x
1
>>> y
2
>>> z
3
>>> ###
>>> 'n'
'n'
>>> '\n'
'\n'
>>> x=2
>>> y=3
>>> c=x+y
>>> print("sum is\n"c)
SyntaxError: invalid syntax
>>> print("sum is\n",c)
sum is
 5
>>> ###
>>> print("A\nB\nC\nD\nE\nF\n")
A
B
C
D
E
F

>>> ###
>>> x=2
>>> print("x")
x
>>> print('x')
x
>>> print(x)
2
>>> print("x+1")
x+1
>>> print('x'+1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('x'+1)
TypeError: must be str, not int
>>> print(x+1)
3
>>> ###
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:3
>>> print("circumference is",c)
circumference is 0.0
>>> eval("x+1")
3
>>> eval("x")
2
>>> r=float(input("Enter the radius"))
Enter the radius3.2
>>> print("circumference is",c)
circumference is 0.0
>>> c.py
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.py
AttributeError: 'float' object has no attribute 'py'
>>> E:/sanjana/c.py
SyntaxError: invalid syntax
>>> E:\sanjana\c.py
SyntaxError: unexpected character after line continuation character
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:2.3
>>> 
KeyboardInterrupt
>>> print("circumference is",c)
circumference is 20.096000000000004
>>> 2*3.14*2.3
14.443999999999999
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 14.443999999999999
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 0.0
>>> r=1
>>> PI=3.14
>>> c=2*PI*r
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>>  print("circumference is",c)
 
SyntaxError: unexpected indent
>>> print("circumference is",c)
circumference is 6.28
>>> ###
>>> a=0
>>> while(a<100):
	print("*",end=")
	      
SyntaxError: EOL while scanning string literal
>>>  while(a<100):
	print("*",end=");
	      
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:3
circumference is 12.56
>>> 2*3.14*3
18.84
>>> 2*3.14*1
6.28
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
2.3
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: could not convert string to float: 
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2.3
circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print("*",end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print('*',end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 4
    a+=1
    ^
IndentationError: unexpected indent
>>> Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ###
>>> x=6
>>> x
6
>>> print(6)
6
>>> print("6")
6
>>> print(x)
6
>>> ###
>>> x=7
>>> x
7
>>> print(x)
7
>>> print("x")
x
>>> ###
>>> 10=x
SyntaxError: can't assign to literal
>>> x=10
>>> x
10
>>> ###
>>> x,y,z=1,2,3
>>> x
1
>>> y
2
>>> z
3
>>> ###
>>> 'n'
'n'
>>> '\n'
'\n'
>>> x=2
>>> y=3
>>> c=x+y
>>> print("sum is\n"c)
SyntaxError: invalid syntax
>>> print("sum is\n",c)
sum is
 5
>>> ###
>>> print("A\nB\nC\nD\nE\nF\n")
A
B
C
D
E
F

>>> ###
>>> x=2
>>> print("x")
x
>>> print('x')
x
>>> print(x)
2
>>> print("x+1")
x+1
>>> print('x'+1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print('x'+1)
TypeError: must be str, not int
>>> print(x+1)
3
>>> ###
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:3
>>> print("circumference is",c)
circumference is 0.0
>>> eval("x+1")
3
>>> eval("x")
2
>>> r=float(input("Enter the radius"))
Enter the radius3.2
>>> print("circumference is",c)
circumference is 0.0
>>> c.py
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.py
AttributeError: 'float' object has no attribute 'py'
>>> E:/sanjana/c.py
SyntaxError: invalid syntax
>>> E:\sanjana\c.py
SyntaxError: unexpected character after line continuation character
>>> PI=3.14
>>> c=2*PI*r
>>> r=eval(input("please enter circle radius:"))
please enter circle radius:2.3
>>> 
KeyboardInterrupt
>>> print("circumference is",c)
circumference is 20.096000000000004
>>> 2*3.14*2.3
14.443999999999999
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 14.443999999999999
>>> r=0
>>> PI=3.14
>>> c=2*PI*r
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>> print("circumference is",c)
circumference is 0.0
>>> r=1
>>> PI=3.14
>>> c=2*PI*r
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>>  r=int(input("please enter circle radius:"))
 
SyntaxError: unexpected indent
>>> r=int(input("please enter circle radius:"))
please enter circle radius:2
>>>  print("circumference is",c)
 
SyntaxError: unexpected indent
>>> print("circumference is",c)
circumference is 6.28
>>> ###
>>> a=0
>>> while(a<100):
	print("*",end=")
	      
SyntaxError: EOL while scanning string literal
>>>  while(a<100):
	print("*",end=");
	      
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2
circumference is 12.56
>>>  exec(open("E:\sanjana\\c.py").read())
 
SyntaxError: unexpected indent
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:3
circumference is 12.56
>>> 2*3.14*3
18.84
>>> 2*3.14*1
6.28
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
2.3
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: could not convert string to float: 
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:2.3
circumference is 0.0
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print("*",end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\c.py").read())
Enter radius:
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    exec(open("E:\sanjana\\c.py").read())
  File "<string>", line 4, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print('*',end=")
                   ^
SyntaxError: EOL while scanning string literal
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 4
    a+=1
    ^
IndentationError: unexpected indent
>>> exec(open("E:\sanjana\\astric.py").read())
	  
SyntaxError: invalid syntax
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print('*'end=")
               ^
SyntaxError: invalid syntax
>>> exec(open("E:\sanjana\\astric.py").read())
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    exec(open("E:\sanjana\\astric.py").read())
  File "<string>", line 3
    print('*'end=")
               ^
SyntaxError: invalid syntax
>>> exec(open("E:\sanjana\\astric.py").read())
*
1
*
2
*
3
*
4
*
5
*
6
*
7
*
8
*
9
*
10
*
11
*
12
*
13
*
14
*
15
*
16
*
17
*
18
*
19
*
20
*
21
*
22
*
23
*
24
*
25
*
26
*
27
*
28
*
29
*
30
*
31
*
32
*
33
*
34
*
35
*
36
*
37
*
38
*
39
*
40
*
41
*
42
*
43
*
44
*
45
*
46
*
47
*
48
*
49
*
50
*
51
*
52
*
53
*
54
*
55
*
56
*
57
*
58
*
59
*
60
*
61
*
62
*
63
*
64
*
65
*
66
*
67
*
68
*
69
*
70
*
71
*
72
*
73
*
74
*
75
*
76
*
77
*
78
*
79
*
80
*
81
*
82
*
83
*
84
*
85
*
86
*
87
*
88
*
89
*
90
*
91
*
92
*
93
*
94
*
95
*
96
*
97
*
98
*
99
*
100
>>> ###
>>> s=str(input("Enter the string:"))
Enter the string:sanjana
>>> name=s
>>> name
'sanjana'
>>> ###
>>> s=str(input("Enter the string:"))
Enter the string:sanjana
>>> t=int(input("Enter the age:"))
Enter the age:19
>>> c='s'+t
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    c='s'+t
TypeError: must be str, not int
>>> c=s+t
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    c=s+t
TypeError: must be str, not int
>>> c='s'+'t'
>>> c
'st'
>>> c=(s+t)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    c=(s+t)
TypeError: must be str, not int
>>> print(str(s)+str(t))
sanjana19
>>> print(str(s)  +  str(t))
sanjana19
>>> print(str(s)+\tstr(t))
SyntaxError: unexpected character after line continuation character
>>>  print(str(s)+\t+str(t))
 
SyntaxError: unexpected indent
>>> print(str(s)+\t+str(t))
SyntaxError: unexpected character after line continuation character
>>> print(str(s)\t+str(t))
SyntaxError: unexpected character after line continuation character
>>>  print("name is:",str(s)+"age is:",str(t))
 
SyntaxError: unexpected indent
>>> print("name is:",str(s)+"age is:",str(t))
name is: sanjanaage is: 19
>>> print("name is:",str(s)+ "age is:",str(t))
name is: sanjanaage is: 19
>>> print("name is:",str(s)+"  "+"age is:",str(t))
name is: sanjana  age is: 19
>>> ###
>>> x=dog
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    x=dog
NameError: name 'dog' is not defined
>>> x="dog"
>>> y="cat"
>>> x+y
'dogcat'
>>> "the"+x+"chase the"+y
'thedogchase thecat'
>>> x*4
'dogdogdogdog'
>>> ###
>>> length=2
>>> length
2
>>> _width=2
>>> _width
2
>>> firstBase=3
>>> firstBase
3
>>> 2MoreToGo=2
SyntaxError: invalid syntax
>>> halt=2
>>> halt
2
>>> halt!=2
False
>>> ###
>>> data=[5,3,7]
>>> data[2]
7
>>> data[-1]
7
>>> len(data)
3
>>> data[0:2]
[5, 3]
>>> 0 in data
False
>>> data+[2,10,5]
[5, 3, 7, 2, 10, 5]
>>> tuple(data)
(5, 3, 7)
>>> ###
>>> exec(open("E:\sanjana\\star.py").read())
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    exec(open("E:\sanjana\\star.py").read())
FileNotFoundError: [Errno 2] No such file or directory: 'E:\\sanjana\\star.py'
>>> exec(open("E:\sanjana\\star.py").read())
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    exec(open("E:\sanjana\\star.py").read())
  File "<string>", line 1
    for(i=1;i<=5;i++):
         ^
SyntaxError: invalid syntax
>>> exec(open("E:\sanjana\\star.py").read())
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    exec(open("E:\sanjana\\star.py").read())
  File "<string>", line 1
    for(int i=1;i<=5;i++):
            ^
SyntaxError: invalid syntax
>>> 
