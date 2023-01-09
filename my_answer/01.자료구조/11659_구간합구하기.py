# point1 : 구간합 배열 인덱스 0값을 0으로 넣어주는게 포인트!
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
N_arr = list(map(int, input().split()))
A = [0]
temp = 0
for i in N_arr:
    temp += i
    A.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(A[j]-A[i-1])