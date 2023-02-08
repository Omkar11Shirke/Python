#(1)
a=7
b=1
for i in range(1,a+1):
  b=b+1
  for j in range(1,i):
    print(b-2)
    
    
#(2)
a=7
b=2
for i in range(a+1,1,-1):
  b=b+1
  for j in range(1,i):
    print(b-2)
    
#(3)
a=7
for i in range(1,a+1):
  b=1
  for j in range(1,i):
    print(b)
    b=b+1
