#(1)(User Defined Functions)
num = 24
print(num)
 
if (num % 3 == 0):
  print("Is multiple of 3")
else:
  print( " Is not multiple of 3")
  
  
#(2)(User Defined Functions)
n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)
       
      
#(3)
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
if __name__ == '__main__':
     
    dec_val = 45

    DecimalToBinary(dec_val)
    
    
#(4)(Boolean Function)
num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
    
    
#(5)(Recursive Functions)
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  

num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))  
