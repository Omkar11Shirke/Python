#1
name=input("Enter a Name: ")
names=[]
for char in name:
  names.append(char)

name=""
for i in range(len(names)-1,-1,-1):
  name=name+names[i]

print(name)

#2
a = "My Name is Omkar"
print ("String : " + a)
res = len(a.split())
print ("Total number of words : " + str(res))

#3
import re
def check_pass(password):
  if len(password)  >= 8 and len(re.findall("[A-Z]",password))>0 and len(re.findall("[0-9]",password))>0:
    print("Criteria Satisfied")
  else:
    print("Error: Password doesn't meet the criteria")

password=input("Enter Password: ")
check_pass(password)

#4
def isPalindrome(a):	
	rev = ''.join(reversed(a))
	if (a == rev):
		return True
	return False
a = "omkar"
ans = isPalindrome(a)
if (ans):
	print("True")
else:
	print("False")
