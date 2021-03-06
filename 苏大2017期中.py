def not_prime(x):
    i = 2
    while i*i < x:
        if x % i == 0:
            return 1
        i += 1
    return 0

num = []
a = input().split()
for i in range(len(a)-1):
    if i % 2 == 0:
        num.append(eval(a[i]+a[i+1]))
    i += 1

num=list(set(num))
a=[]
for item in num:
    if not_prime(item)==0:
        a.append(item)
n = len(a)
for i in range(n-1):
    for j in range(i+1, n):
        if(a[i]%10+(a[i]%100)//10 < a[j]%10+(a[j]%100) //10):
            a[i], a[j] = a[j], a[i]

for i in range(n):
    print('%10s'%a[i],end='')
    if i % 2==1:
        print()
print()
print('Max=%d'%max(a))
print('Min=%d'%min(a))
print('aver=%.3f'%float(sum(a)/len(a)))