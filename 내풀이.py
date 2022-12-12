def solution(n, computers):
    answer = 0
    visited = [0] * n
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    print(answer)
    return answer

from collections import deque
def solution(tickets):
    answer = []
    arr = []
    d = deque(tickets)
    visited = [False] * len(tickets)
    for idx,value in enumerate(d):
        result_arr = dfs(len(tickets),d,idx,visited)
        if result_arr is not None:
            arr.append(result_arr)
        visited = [False for i in range(len(tickets))]
    arr = sorted(arr)
    answer = arr[0]
    print(answer)
    return answer
def dfs(num,tickets,idx,visited):
    stack = []
    array = []
    alpha = []
    visited[idx] = True
    stack.append(tickets[idx])
    while stack:
        tmp_stack = stack.pop()
        array.append(tmp_stack[0])
        if False not in visited:
            array.append(tmp_stack[1])
        if num+1 == len(array):
            return array
        for index,value in enumerate(tickets):
            if visited[index] == False and tmp_stack[1] == value[0]:
                visited[index] = True
                alpha.append(value)
                if len(alpha) > 1:
                    alpah = sorted(alpha)
                    stack.append(value)
                else:
                    stack.append(value)
                
            
                
        
        
       
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
from collections import deque
def solution(tickets):
    answer = []
    arr = []
    d = deque(tickets)
    visited = [False] * len(tickets)
    for idx,value in enumerate(d):
        result_arr = dfs(len(tickets),d,idx,visited)
        if result_arr is not None:
            arr.append(result_arr)
        visited = [False for i in range(len(tickets))]
    arr = sorted(arr)
    answer = arr[0]
    print(answer)
    return answer
def dfs(num,tickets,idx,visited):
    stack = []
    array = []
    alpha = []
    visited[idx] = True
    stack.append(tickets[idx])
    while stack:
        tmp_stack = stack.pop()
        array.append(tmp_stack[0])
        if False not in visited:
            array.append(tmp_stack[1])
        if num+1 == len(array):
            return array
        for index,value in enumerate(tickets):
            if visited[index] == False and tmp_stack[1] == value[0]:
                stack.append(value)
                visited[index] = True
                break

[
    ['AAA', 'ICN', 'AAA', 'ICN', 'ICN', 'AAA'], 
    ['AAA', 'ICN', 'AAA', 'ICN', 'ICN', 'AAA'], 
    ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA'], 
    ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA'], 
    ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA']
]
   # ['AAA', 'ICN', 'AAA', 'ICN', 'ICN', 'AAA']


from collections import defaultdict 
def dfs(graph, N, key, footprint):
    print(footprint)
    if len(footprint) == N + 1:
        return footprint
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)
        tmp = footprint[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)
        graph[key].insert(idx, country)
        if ret:
            return ret

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()
    answer = dfs(graph, N, "ICN", ["ICN"])
    return answer

from collections import deque
def solution(tickets):
    answer = []
    arr = []
    d = deque(tickets)
    visited = [False] * len(tickets)
    for idx,value in enumerate(d):
        result_arr = dfs(len(tickets),d,idx,visited)
        if result_arr is not None:
            arr.append(result_arr)
        visited = [False for i in range(len(tickets))]
    arr = sorted(arr)
    answer = arr[0]
    print(answer)
    return answer
def dfs(num,tickets,idx,visited):
    stack = []
    array = []
    alpha = []
    visited[idx] = True
    stack.append(tickets[idx])
    while stack:
        tmp_stack = stack.pop()
        array.append(tmp_stack[0])
        if False not in visited:
            array.append(tmp_stack[1])
        if num+1 == len(array):
            return array
        for index,value in enumerate(tickets):
            if visited[index] == False and tmp_stack[1] == value[0]:
                visited[index] = True
                alpha.append(value)
                if len(alpha) > 1:
                    alpha = sorted(alpha)
                    stack.append(alpha[0])
                    alpha = []
                    break
                else:
                    tmp = value
            if (len(tickets)-1) == index:
                stack.append(tmp)
                
                
solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]])
#["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

from collections import deque
def solution(begin, target, words):
    answer = 0
    d = deque(words)
    d.remove(target)
    d.appendleft(target)
    answer = dfs(begin,target,d,0)
    print(answer)
    return answer
def dfs(begin,target,words,cnt):
    cntA = 0
    ans = 0
    for index,value in enumerate(words):
        for beginA, targetA, wordsA in zip(begin, target, value):
            if beginA == wordsA:
                cntA += 1
        if cntA == 2:
            cntA = 0
            if value == target:
                return cnt
            else:
                words.remove(value)
                ans = dfs(value,target,words,cnt+1)
        cntA = 0
    return ans
                
solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
#solution("hit",    "cog",  ["hot", "dot", "dog", "lot", "log"])
from collections import deque
def solution(queue1, queue2):
    answer = 0
    chk = False
    d1 = deque(queue1)
    d2 = deque(queue2)
    startData = 0 
    endData = 0
    listAll = queue1+queue2
    hap = sum(d1) + sum(d2)
    val = int(hap/2)
    for start in range(len(listAll)):
        for end in range(len(listAll)+1):
            if start < end:
                if val == sum(listAll[start:end]):
                    startData = start
                    endData = end
                    chk = True
                    break
        if chk == True:
            break
    if startData == 0 and endData == 0:
        return -1
    else:
        answer = startData + (endData-len(queue2))
    return answer
#solution([3, 2, 7, 2],[4, 6, 5, 1])
solution([1, 2, 1, 2],[1, 10, 1, 2])
#solution([1, 1],[1, 5])
#solution([1, 2],[1, 2])
from collections import deque
def solution(queue1, queue2):
    answer = 0
    val = int(sum(queue1+queue2)/2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    leftSum = sum(queue1)
    while queue1 and queue2:
        if leftSum > val:
            tmp = queue1.popleft()
            leftSum -= tmp
        elif leftSum < val:
            tmp = queue2.popleft()
            queue1.append(tmp)
            leftSum += tmp
        else:
            return answer
        answer += 1
            
    return -1
solution([3, 2, 7, 2],[4, 6, 5, 1])
#solution([1, 2, 1, 2],[1, 10, 1, 2])
#solution([1, 1],[1, 5])
#solution([1, 2],[1, 2])
def solution(n, lost, reserve):
    answer = 0
    check = 0
    reserveLen = len(reserve)
    setA = set(lost) | set(reserve)
    remain = n - len(setA)
    lost = sorted(lost)
    reserve = sorted(reserve)
    for lostVal in lost:
        if lostVal not in reserve:
            if lostVal-1 in reserve and lostVal-1 not in lost:
                reserve.remove(lostVal-1)
            
            elif lostVal+1 in reserve and lostVal+1 not in lost:
                reserve.remove(lostVal+1)
    
            else:
                continue
            check += 1
    answer = remain + check + reserveLen
    return answer
#solution(5,[2, 4],[1, 3, 5])
#solution(3,[3],[1])
solution(4,[2,3],[3,4])

def solution(name):
    answer = 0
    alphabat = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":12,"P":11,"Q":10,"R":9,"S":8,"T":7,"U":6,"V":5,"W":4,"X":3,"Y":2,"Z":1}
    visited = [False] * len(name)
    for index,nameVal in enumerate(name):
        if nameVal == 'A':
            visited[index] = True
    print(visited)    
    for value in name:
        answer += alphabat[value]
    answer += len(name) - 1
    return answer
solution("JAN")
import time
answer = 0
def solution(people, limit):
    visited = [False] * len(people)
    for idx in range(len(people)):
        if visited[idx] == False:
            start_time = time.time() # 측정 시작
            dfs(people, limit, idx, visited)
            end_time = time.time() # 측정 종료
            print("time:", end_time - start_time) # 수행 시간 출력
    print(answer)
    return answer
def dfs(people, limit, idx, visited):
    global answer
    visited[idx] = True
    tmp_val = 0
    tmp_idx = 0
    check = True
    for val in range(len(people)):
        if limit >= people[idx] + people[val] and visited[val] == False:
            if check:
                tmp_val = people[val]
                tmp_idx = val
                check = False
            if people[val] > tmp_val:
                tmp_val = people[val]
                tmp_idx = val
    if tmp_val != 0:
        visited[tmp_idx] = True
    answer += 1
#solution([70, 50, 80, 50],100)
solution([40,50,150,160],200)

#from collections import deque
sum = 0
def solution(v):
    n = len(v)
    m = len(v[0])
    answer = []
    for i in range(len(v)):
        for j in range(len(v[i])):
            if dfs(i,j) == True:
                result += 1
    print(result)
def dfs(x, y):
    global n
    global m
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] == 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
solution([[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]])


