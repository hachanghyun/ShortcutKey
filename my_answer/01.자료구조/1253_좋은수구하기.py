# point1 : start 1씩 증가시키고, end 1씩 감소시키면서 find랑 비교하는게 포인트!
# point2 : 비교값이 i,j랑 같지않는 조건 넣어주는게 포인트!
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
result = 0
for k in range(N):
    find = A[k]
    i = int(0)
    j = int(N-1)
    while i < j :
        if A[i] + A[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1    
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(result)