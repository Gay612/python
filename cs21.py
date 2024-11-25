

a=input('enter your month')
b=[a.strip() for m in a.split(',')]
for i in b:
     if i == 'feb':
        print(i,'has 28 days')
     elif i in('jan','mar','may','july','aug','oct','dec'):
        print(i,'has 31 days')
     elif i in('april','june','sept','nov'):
        print(i,'has 30 days')
     else:
        print(i,'has invalid month')
