n1=int(input("Enter the marks of n1:"))
n2=int(input("Enter the marks of n2:"))
n3=int(input("Enter the marks of n3:"))
n4=int(input("Enter the marks of n4:"))
n5=int(input("Enter the marks of n5:"))
avg=n1+n2+n3+n4+n5/5
print(avg)
if(avg>=80):
    print("o grade")
elif(avg<=80 and avg>=70):
    print("A +")
elif(avg<=70 and avg>=60):
    print("A grade")
elif(avg<=60 and avg>=50):
    print("B +")
elif(avg<=50 and avg>=40):
    print("B")
else:
    print("Fail")
