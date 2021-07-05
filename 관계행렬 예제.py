import numpy as np
from utils.functionCheck import vali
A = [1,2,3,4,8]
B = A

R = []

for a in range(len(A)):
    for b in range(len(B)):
        if A[a]+B[b]<=9:
            R.append((a,b))

M = np.zeros((len(A), len(B)))

for (a,b) in R:
    M[a][b] = 1
    print(str(A[a])+'->'+str(B[b]))

RE = []
for (a,b) in R:
    RE.append((A[a],B[b]))
ANS = vali(A,B,RE)

print('정의역:', ANS[0])
print('치역:',ANS[1])
print('공변역:',ANS[2])

print(M)
