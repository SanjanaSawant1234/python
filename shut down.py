def shut_down(s):
    if(s=="yes"):
        return("shutting down")
    elif(s=="no"):
        return("shutdown aborted")
    else:
        return("sorry")
a=input("want to shut down:")   
print(shut_down(a))
