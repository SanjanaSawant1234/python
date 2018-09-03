def num():
    s=list()

    for i in range(1,21):
       p=i**2
       s.append(p)
    print(s)
    print("first five",s[0:5])
    print("last five",s[-5:])
num()
