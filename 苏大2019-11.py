import math

def func1(x):
    if x>=60:
        return True
    return False

def func2(n):
    ans=0
    while n-50>=0:
        n-=50
        ans+=8
    while n-30>=0:
        n-=30
        ans+=4
    return ans+n//10

if __name__=="__main__":
    #print(func1(80))
    print(func2(90))