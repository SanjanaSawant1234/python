jvm_langs=['java','jpython','groovy','scala','jruby']
print('I know of',jvm_langs.__len__(),'langs that can run on jvm')
print('I know of',len(jvm_langs),'langs that can run on jvm')
print('oops i forgot clojure')
jvm_langs.append('clojure')
for lang in jvm_langs:
    print (lang)
print("the 3rd jvm language is",jvm_langs[2])
print("the first 3 jvm language is",jvm_langs[:3])
print("the 2nd to 4th jvm language is",jvm_langs[1:4])
print("lets sort these languages")
jvm_langs.sort()
print (jvm_langs)
    

