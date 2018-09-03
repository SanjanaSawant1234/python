s=input("Enter the string:")
result="  "
for i in range(0,len(s),2):
    if s[i].isupper():
        result+=s[i]
print(result)
