import math


def func1(m, n):
    if m <= 1 or n <= 1:
        return
    for i in range(2, min(m, n)):
        if m % i == 0 and n % i == 0:
            return True
    return False


def func2(a):
    n = len(a)
    sum = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]: sum += 1
    return sum


def func3(mat1, mat2):
    ans = []
    m = len(mat1)
    d = len(mat1[0])
    n = len(mat2[0])
    for i in range(m):
        L = []
        for j in range(n):
            sum = 0
            for k in range(d):
                sum += mat1[i][k] * mat2[k][j]
            L.append(sum)
        ans.append(L)
    return ans


def func4(a):
    n = int(math.sqrt(len(a)))
    ans = []
    for i in range(n):
        L = []
        for j in range(n):
            L.append(a[i * n + j])
        ans.append(L)
    return ans


def func5(st):
    a = []
    a = st.split()
    M = {}
    for item in a:
        if M.get(item):
            M[item] += 1
        else:
            M[item] = 1
    m = sorted(M.items(), key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(min(len(m), 3)):
        ans.append(m[i][0])
    return ans


def func6(st1, st2):
    a = 0
    b = 0
    c = 0
    for i in range(26):
        ch = chr(ord('a') + i)
        if ch in st1 and ch in st2:
            a += 1
        if ch in st1 and ch not in st2:
            b += 1
        if ch not in st1 and ch in st2:
            c += 1
    return list([a, b, c])


def func7(st):
    st = st.upper()
    # return st
    n = len(st)
    M = {}
    for ch in st:
        if M.get(ch):
            M[ch] += 1
        else:
            M[ch] = 1
    m = sorted(M.items(), key=lambda x: x[1], reverse=True)
    # print(m[0][0],m[0][1])
    return list([m[0][0], m[0][1]])


def work(st):
    n = len(st)
    sum = 0
    for i in st:
        sum += ord(i)
    return sum / n


def func8(st):
    n = len(st)
    str = ""
    a = []
    for ch in st:
        if ch < '0' or ch > '9':
            str += ' '
        else:
            str += ch
    m = str.split()
    for item in m:
        if 3 <= len(item) <= 5:
            a.append(item)
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if work(a[i]) < work(a[j]):
                a[i], a[j] = a[j], a[i]
    return a


if __name__ == "__main__":
    # print(func1(-1,46))
    # print(func2([1,3,2,4]))
    # print(func3([[1,2],[1,3]],[[1,1],[1,0]]))
    # print(func4([1,2,3,4]))
    # print(func5('a'))
    # print(func6("his", "she"))
    # print(func7("1aA"))
    # print(func8("123a4567 1"))
