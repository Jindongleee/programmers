def solution(d, budget):
    
    # d는 부서별 신청 예산 금액
    # budget은 총 예산
    
    # answer = 최대 지원 가능한 부서 개수
    count = 0
    # for i in d:
    #     if((budget - i) >= 0):
    #         count += 1
    #     budget -= i
    total = sum(d)
    d.sort()
    print(d)
    
    i=0
    while True:        
        if i==len(d):
            break
            
        budget -= d[i]
        if(budget < 0):
            break
        else:
            i+=1

        
    return i