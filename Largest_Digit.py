n=int(input())
w=n%10
n=n//10
x=n%10
n=n//10
y=n%10
n=n//10
z=n%10
n=n//10
if(w>x and w>y and w>z):
     print(w)
elif(x>w and x>y and x>z):
      print(x)
elif(y>x and y>w and y>z):
      print(y)
else:
      print(z)