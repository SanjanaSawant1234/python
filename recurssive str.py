def add(x,y):
    q=x+y
    return ('the sum of {} and {} is {}'.format(x,y,q))

def main():
    print(add(4,5))
    print(add(32543564,35436346))
    n1=int(input("Enter an integer:"))
    n2=int(input("Enter an integer:"))
    print(add(n1,n2))
main()
