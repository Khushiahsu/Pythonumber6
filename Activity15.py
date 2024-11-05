#Identify Operator

a=[1,2,3,4,5,6,7]  
b=[1,2,3,4,5,6,7]
c=a
print(c is  a)
print(b is  a)

print(c is not a)
print(b is not a) 

x = ['a','b','c','d','e','f','g','h','i']
y = ['a','b','c','d','e','f','g','h','i']
z = x
print(x is z)
print(y is x)
print(z is not x)
print(x is not y)


q=12

if (type(q) is int):
    print(" You are correct")

else:
    print("Hard luck")
m = 15.5

if (type(m) is float):
    print(' You got the answer correct!')
else:
    print(' You did not do it right')



#####################################################################################

#Membership Operator

a=[1,2,3,4,5,6,7]  
b=[1,2,3,4,5,6,7]
c=a
print(c in  a)
print(b in  a)

print(c  not in  a)
print(b  not in  a) 

v = "AARAV"
r = "AARAV"
l = v
print(v in l)
print(v in r)
print(v not in l)
print(v not in r)