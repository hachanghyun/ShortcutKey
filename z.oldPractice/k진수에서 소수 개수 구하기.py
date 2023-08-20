import math

#n진수 구하는 함수
def nsolution(n, q): #값, q진수
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

#소수 구하는 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    answer = 0
    nData = nsolution(n, k)
    arr = nData.split('0')
    arr = [v for v in arr if v]
    for i in arr:
        if i != '1':
            if True == is_prime_number(int(i)):
                answer += 1
    print(answer)
    return answer

#solution(437674,3)
solution(110011,10)
