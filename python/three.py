def triangles():
    A = [1]
    B = [1]
    C = [1]
    D = [1]
    E = [1]
   # x = 0
    while True:
        yield (E)
        A = C
        A.append(0)
        B = D
        B.insert(0,0)
        C = []
        D = []
        E = []
        for x in range(len(A)):
            C.append(A[x]+B[x])
            D.append(A[x]+B[x])
            E.append(A[x]+B[x])
            
        


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')