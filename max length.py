def maxlength():
    x=input("Enter the string:")
    y=input("Enter the string:")
    if(x>y):
        print(x)
    elif(len(x)==len(y)):
        print("strings are equal\n",x,"\n",y)
    else:
        print(y)

maxlength()
    
