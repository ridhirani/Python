#division
import operator # the operator module provides 2-argument arithmetic functions
a=4
b=1
c=3.0
print(operator.truediv(a, b)) # = 1.5
print(operator.floordiv(a, b)) # = 1
print(operator.floordiv(a, c)) # = 1.0

#addition
l1=[1,2,3]
l2=[4,5]
print(l1+l2)

s1="hello"
s2="ridhi"
print(s1+' '+s2)

#Exponentiation
a,b=2,3
print((a ** b))
print(pow(a,b))

a,b,c=2,3,4 #here we are using built in pow() it will read pow(a,b,c) as( a ** b ) % c 
print(pow(a,b,c)) 

#square root
import math,cmath
a=4
print(math.sqrt(a)) #it will give result in float
print(cmath.sqrt(a))  #cmath will give result in complex no