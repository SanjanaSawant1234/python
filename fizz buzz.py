def abc():
    n=int(input("Enter the number:"))
    if(n%3==0):
        print("fizz")
    if(n%5==0):
        print("buzz")
    if(n%3==0 and n%5==0):
        print("fizzbuzz")

abc()
