import math 
x=0
a0=7.86
a=16.67
b=76.667
L=99
for n in range(5,30):
  eq=a*math.cos(math.cos (n*math.pi*x)/L) + b*math.sin(math.sin(n*math.pi*x)/L)
eq2=a0+eq
print("Final Values is: ",eq2)
