from collections import OrderedDict 
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
print('before deleting')
for key , value in od.items():
    print(key,value)
od.pop('a')
od['a']=1
print('after re inserting')
for key,value in od.items():
    print(key,value)
