n=int(input())
m=n%10
n=n//10
r=n%10
n=n//10
k=n%10
n=n//10
if(m%2==0 and r%2==0 and k%2==0):
    print("Even")
elif(m%2!=0 and r%2!=0 and k%2!=0):
    print("Odd")
else:
    print("Mixed")