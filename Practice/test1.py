import string
def solution(n):
    answer = ''
    print(sol(10, 3))
    return answer

def sol(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


solution(78)

1
2
10
11
12
20
21
22
100
101