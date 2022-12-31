#소수판별 
import math
def primenumber(x):
    for i in range (2, int(math.sqrt(x)) + 1):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:      # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True 
#순열
from itertools import permutations
for i in permutations([1,2,3,4], 2):
    print(i, end=" ")
#조합
from itertools import combinations
for i in combinations([1,2,3,4], 2):
    print(i, end=" ")
#리스트 배열을 문자열로 바꾸기
a = []
string = ''.join(a)
#소인수분해 구하기
def factorize(n):
    factor = 2      
    factors = []    
    
    while (factor**2 <= n):           
        while (n % factor == 0):      
            n = n // factor            
            factors.append(factor)
        factor += 1
    
    if n > 1:
        factors.append(n)
    
    return factors
#리스트 요소값 곱하기1
from functools import reduce
reduce(lambda x,y : x*y, [1,2,3,4,5])
#리스트 요소값 곱하기2
from math import prod
prod([1,2,3,4,5])
#리스트 n개로 분할하기
def list_chuck(arr, n):
    return [arr[i: i + n] for i in range(0, len(arr), n)]
array = [1, 2, 3, 4, 5, 6, 7, 8]
result_array = list_chuck(array, 3)
print(result_array)        # [[1, 2, 3], [4, 5, 6], [7, 8]]
#리스트 인덱스, 원소 같이 출력
for i, letter in enumerate(['A', 'B', 'C'], start=1):
    print(i, letter)
'''1 A
   2 B
   3 C'''
#Key, Value 쌍 얻기(items)
answer = [k for k, v in dic.items() if v == 1] 
#Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth']) #a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다.
#Value 리스트 만들기(values)
a.values()
dict_values(['pey', '0119993323', '1118'])
#value로 키 찾기
[k for k, v in dictP.items() if v == 1]
#딕셔너리안에 키 값 있는지 찾기
if val in dictP:
#딕셔너리 컨프리헨션
d = {e:[] for e in set(genres)}
d[e[0]].append([e[1] , e[2]])
#try: except
    try:
        st.pop()
    except :
        return False

#heap 리스트에서 최소원소 추출하는 자료구조
import heapq
heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print(heap)
#heappop 함수는 가장 작은 원소를 힙에서 제거함과 동시에 그를 결괏값으로 리턴한다.
result = heapq.heappop(heap)
print(result)
print(heap)
#deque
from collections import deque
d = deque()
d.appendleft(0)
d.append(6)
d.popleft()
d.pop()
# 리스트 인덱스
listA = [1,2,3,4,5]
print(listA[1:4])
#집합 자료형
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = s1 & s2
print(s3)   #result : {4,5,6}
s3 = s1 | s2
print(s3)   #result : {1, 2, 3, 4, 5, 6, 7, 8, 9}
s3 = s1 - s2
print(s3)   #result : {1, 2, 3}
s3 = s2 - s1
print(s3)   #result : {8, 9, 7}
#defaultdict


