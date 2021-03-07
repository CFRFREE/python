"""
作者:FREE
日期:2021年03月06日
"""
import math
from datetime import date

def func1(y,m,d):
    try:
        date(y,m,d)
    except:
        return -1
    else:
        d=date(y,m,d)
        st=d.strftime('%j')
        while st[0]=='0':
            st=st[1:]
        return st

def func2(m,n):
    for i in range(m+1):
        if i*2+(m-i)*4==n:
            return tuple((i,m-i))
    return

def func3(a):
    a=sorted(a)
    n=len(a)
    if n<=1:
        return
    for i in range(1,n):
        if a[i]-a[i-1]!=a[1]-a[0]:
            return False
    return True

def func4(a):
    n=len(a)
    if n==0:
        return
    for i in a:
        if type(i)!='int':
            return
        if i!=int(i):
            return
    a=sorted(a)
    if n%2==1:
        return a[n//2]
    else:
        return (a[n//2]+a[n//2-1])//2

def func5(st):
    a=[]
    st=st.lower()
    a=st.split( )
    ans=""
    n=len(a)
    if n<3 or n>11:
        return
    for i in a:
        if i=='zero':
            ans+='0'
        if i=='one':
            ans+='1'
        if i=='two':
            ans+='2'
        if i=='three':
            ans+='3'
        if i=='four':
            ans+='4'
        if i=='five':
            ans+='5'
        if i=='six':
            ans+='6'
        if i=='seven':
            ans+='7'
        if i=='eight':
            ans+='8'
        if i=='nine':
            ans+='9'
    return ans

def func6(a,b,c,d):
    ans=set()
    for x in range(a,b+1):
        for y in range(c,d+1):
            ans.add(y/x)
    return len(ans)

def func7(s1,s2,n):
    m=len(s1)//n
    if m*n!=len(s1):
        m+=1
    ans=""
    for i in range(m):
        for j in range(n):
            if len(s1)==0:
                ans+=' '
            else:
                ans+=s1[0]
                s1=s1[1:]
        ans+=s2
    return ans

def func8(st):
    n=len(st)
    ans=""
    while len(st)!=0:
        if st[0]!='<':
            ans+=st[0]
            st=st[1:]
        else:
            pos=st.find('>')
            s=st[1:pos]
            s=s.upper()
            s+='-'
            s+=str(len(s)-1)
            s='['+s+']'
            ans+=s
            st=st[pos+1:]
    return ans


if __name__=="__main__":
    #print(func1(2019,3,991))
    #print(func2(35,111))
    #print(func3([33, -7, 3, 13, 43, 53, 23]))
    #print(func4([1, "abc"]))
    #print(func5("one one two two three three four"))
    #print(func6(1,10,1,10))
    #print(func7("abcd","##",5))
    #print(func8("he defended <_abc>, his decision to <43>"))