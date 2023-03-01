def solution(survey, choices):
    answer = ''
    aAnswer = ["R", "C", "J", "A",]
    sDic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    cDic = {1:3, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3}

    for sur,cho in zip(survey,choices):
        if cho < 4:
            sDic[sur[0]] += cDic[cho]
        elif cho > 4:
            sDic[sur[1]] += cDic[cho]

        if sur[0] == 'R' or sur[1] == 'R':
            if sDic['R'] > sDic['T']:
                aAnswer[0] = 'R'
            elif sDic['R'] < sDic['T']:
                aAnswer[0] = 'T'
            else:
                aAnswer[0] = 'R'

        if sur[0] == 'C' or sur[1] == 'C':
            if sDic['C'] > sDic['F']:
                aAnswer[1] = 'C'
            elif sDic['C'] < sDic['F']:
                aAnswer[1] = 'F'
            else:
                aAnswer[1] = 'C'
        
        if sur[0] == 'J' or sur[1] == 'J':
            if sDic['J'] > sDic['M']:
                aAnswer[2] = 'J'
            elif sDic['J'] < sDic['M']:
                aAnswer[2] = 'M'
            else:
                aAnswer[2] = 'J'

        if sur[0] == 'A' or sur[1] == 'A':
            if sDic['A'] > sDic['N']:
                aAnswer[3] = 'A'
            elif sDic['A'] < sDic['N']:
                aAnswer[3] = 'N'
            else:
                aAnswer[3] = 'A'

    for i in aAnswer:
        answer += i
    print(answer)
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])    

'''
def solution(survey, choices):
    answer = ''
    dCho = {1:3, 2:2, 3:3, 4:0, 5:1, 6:2, 7:3}
    jDict = {"RT" : 0, "CF" : 1, "JM" : 2, "AN" : 3}
    aAnswer = ["R","C","j","A"]
    cAnswer = [0, 0, 0, 0]

    for sur,cho in zip(survey,choices):
        if sur in jDict:
            if cAnswer[jDict[sur]] == 0:
                cAnswer[jDict[sur]] = dCho[cho]    
                if cho < 4:
                    aAnswer[jDict[sur]] = sur[0]
                elif cho > 4:
                    aAnswer[jDict[sur]] = sur[1]               
        else:    
            sur = sur[::-1]
            if cAnswer[jDict[sur]] == 0: 
                cAnswer[jDict[sur]] = dCho[cho]
                if cho < 4:
                    aAnswer[jDict[sur]] = sur[1]
                elif cho > 4:
                    aAnswer[jDict[sur]] = sur[0]
            else:
                if cAnswer[jDict[sur]] > dCho[cho]
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])  
'''