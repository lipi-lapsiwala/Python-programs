def gcd(a,b):
  if(b==0):
    return a
  else:
    return gcd(b,a % b)
    
a = int(input("Enter no 1 : "))
b = int(input("Enter no 2 : "))

ans = gcd(a,b)
print("GCD of %d and %d is : %d" %(a,b,ans))
