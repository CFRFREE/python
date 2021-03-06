"""
作者:FREE
日期:2021年03月02日
"""
def func1(x):
    if x>=0:
        return x*5
    else:
        return  1+3*(-x)

def func2(x):
    if x>=10:
        return 10
    elif x>=8:
        return 8*x**3
    elif x>=3:
        return 3*x**2
    elif x>=0:
        return x+1
    else:
        return -x

def func3(m,n):
    if m>=0 and n>=0 and m<=n and m==int(m) and n==int(n):
        sum3=0
        for i3 in range(m,n+1):
            if i3%2==1:sum3+=i3
        return sum3
    else:
        return

def func4(m,n):
    sum4=0
    for i4 in range(max(0,m),n+1):
        st4=str(i4)
        for ch4 in st4:
            if ch4=='2':
                sum4+=1
    return sum4

def func5(n):
    if int(n)==n and n>0:
        ans1=0
        ans2=0
        ans3=0
        while n>0:
            ans1+=1
            ans2+=n%10
            ans3=max(ans3,n%10)
            n//=10
        return list((ans1,ans2,ans3))
    return

def func6(m,n):
    if int(m)==m and int(n)==n and m>0 and n>0:
        x=m
        i=0
        while x>10:
            x//=10
            i+=1
        m+=n*(10**i)
        if x+n>=10:
            m-=10**(i+1)
        return m
    else:
        return

def func7(k,a):
    if k>len(a):
        return list(reversed(a))
    b=[]
    for i in range(k):
        b.append(a[i])
    b.reverse()
    for i in range(k,len(a)):
        b.append(a[i])
    return b

def func8(v,lst):
    a=[]
    for item in lst:
        x=item
        i=0
        sum=0
        while x>0:
            i+=1
            sum+=x%10
            x//=10
        if sum/i>=v:
            a.append(item)
    a.sort(reverse=True)
    return a

if __name__=="__main__":
    print(func1(-3))
    print(func2(3))
    print(func3(1.5,10))
    print(func4(2,22))
    print(func5(1234))
    print(func6(345,8))
    print(func7(6,[1,2,3,4,5]))
    print(func8(2,[123,1234,1,12,123456,3333]))