import math


def func1(x, y):
    x = abs(x)
    y = abs(y)
    if x == 1 and y <= 1 or y == 1 and x <= 1:
        return 0
    if x < 1 and y < 1:
        return 1
    else:
        return -1


def func2(d, l, r):
    ans = 0
    if d < 0 or d > 9 or l >= r:
        return
    for i in range(l, r + 1):
        x = str(i)
        for ch in x:
            if int(ch) == d:
                ans += 1
    return ans


def prime(x):
    if x <= 1:
        return 0
    i = 2
    while i * i <= x:
        if x % i == 0:
            return 0
        i += 1
    return 1


def func3(a):
    T = []
    for item in a:
        st = str(item)
        T.append(int(st[0]))
        T.append(int(st[-1]))
    ans = []
    now = ""
    for item in T:
        if prime(item):
            if len(now) > 0:
                ans.append(int(now))
            ans.append(item)
            now = ""
        else:
            now += str(item)
    if len(now) > 0:
        ans.append(int(now))
    return ans


def func4(a):
    m = len(a)
    ans = []
    k = (m + 1) // 2
    for s in range(m):
        now = []
        for i in range(m):
            if i > s:
                now.append(0)
            else:
                now.append(a[s - i][i])
        ans.append(now)
    for s in range(m - 2, -1, -1):
        print(s)
        now = []
        for i in range(m):
            if i > s:
                now.append(0)
            else:
                now.append(a[k - i][k - (s - i)])
        ans.append(now)
    return ans


def func5(st):
    if len(st) < 2:
        return
    if st.lower() == st:
        return st[0].upper() + st[1:-2] + st[-1].upper()
    else:
        return st[0].upper() + st[1:].lower()


def func6(st):
    n = len(st)
    s = ""
    for ch in st:
        x = ord(ch)
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            s += ch
        else:
            s += " "
    a = s.split()
    ans = ""
    for item in a:
        st = ""
        if len(item) > 5:
            st = item[0] + '*' * (len(item) - 2) + item[-1]
            ans += st
            ans += " "
        else:
            ans += item
            ans += " "
    return ans[0:-1]


def func7(a, st):
    M = {}
    for ch in st:
        if M.get(ch):
            M[ch] += 1
        else:
            M[ch] = 1
    ans = 0
    for item in a:
        N = M.copy()
        p = 0
        for ch in item:
            if p == 1:
                continue
            if N.get(ch):
                N[ch] -= 1
            else:
                p = 1
        if p == 0:
            ans += 1
    return ans


def func8(a):
    M = {}
    for item in a:
        id = item[0]
        t = item[1]
        flag = 0
        for ch in id:
            if ch < '0' or ch > '9':
                flag = 1
        if flag == 1:
            continue
        if M.get(id):
            M[id] += t
        else:
            M[id] = t
    m = sorted(M.items(), key=lambda x: x[1], reverse=True)
    if len(m) == 0:
        return
    return m[0]


if __name__ == "__main__":
    # print(func1(0,0))
    # print(func2(12,3,6))
    # print(func3([12,34,56,78,90]))
    # print(func4([[1,2], [3,4]]))
    # print(func5("comPUtER"))
    # print(func6("!=-,."))
    # print(func7(["cat","bt","hat","tree"],"atach"))
    # print(func8([('19274056',3),('192740A01',2),('192740101',3)]))
