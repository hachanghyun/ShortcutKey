'''
백준 입력값 default 세팅
'''
N = int(input())
nList = list(map(int,input().split()))
M = int(input())
#a, b = map(int,input().split())
#print(N, M , nList)

'''
구현
'''
answer = 0
sum = 0
maxData = 0
tmpData = 0
startData = M // N 
#print("startData = ", startData)

while True:
    for i in nList:
        if startData > i:
            sum += i
            if i > maxData:
                maxData = i
        else:
            sum += startData
            if startData > maxData:
                maxData = startData

    #print("sum = ", sum)
    tmpData = max(nList)
    if startData > tmpData:
        break;

    if sum >= M:
        #print("상한액 초과")
        break;
    else:
        startData += 1
        sum = 0
        answer = maxData
        maxData = 0

#print("예상최대값")
print(answer)

'''
수도 코드 
상한액 startData = M // N 
반복문
if startData < nList[i]
    sum += nList[i]
else 
    sum += startData

if sum > M 
    전에 sum 호출

M보다 커질때까지 반복문 
M보다 커지면 종료 
answer = nList 중 max값
'''