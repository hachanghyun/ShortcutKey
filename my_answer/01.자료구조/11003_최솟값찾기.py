# point1 : 존나어려움 그냥 유튜브 보고 일단 이해해보자
# point2 : 슬라이딩 윈도우 사용한다함 

# point3 : 최솟값 가능성 없는 데이터 삭제
# point4 : window 크기 밖 데이터 삭제 
# point5 : mydeque [0 or -1] 맨앞 위치, 맨뒤 위치 [0 or 1] 값이랑 인덱스값
from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ')

