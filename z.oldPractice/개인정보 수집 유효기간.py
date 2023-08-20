#pip install python-dateutil
from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    privacies_dict = {}

    # terms 구하기
    for t in terms:
        terms_dict[t.split()[0]] = t.split()[1]

    #today 변환
    tDates = datetime(int(today.split('.')[0]),int(today.split('.')[1]),int(today.split('.')[2]))

    #privacies 구하기
    for p in range(len(privacies)):
        sDate = privacies[p].split()[0]
        sTimes = datetime(int(sDate.split('.')[0]),int(sDate.split('.')[1]),int(sDate.split('.')[2]))
        privacies_dict[privacies[p].split()[0]] = p+1
        monthAgo = sTimes + relativedelta(months = int(terms_dict[privacies[p].split()[1]]))
        
        if tDates >= monthAgo:
            answer.append(privacies_dict[privacies[p].split()[0]])

    return answer

solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])