dict={'a':10,'b':10,'c':239}
s=dict.values()
print(s)
#mult=dict.values()
mult=1
#print(mult)
for key in dict:
    mult=mult*dict[key]
print(mult)


