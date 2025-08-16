def solution(n):
    
    # n이 양의 제곱이라면 -> (n+1)**2 리턴
    # n이 양의 제곱이 아니라면 -> -1 리턴
    
    # 제곱수인지 판단하기
    
    for i in range(n):
        
        if((n%(i+1))==0): # 일단 나눴을 때 나머지 0
            if((n/(i+1)) == (i+1)): # 그 중 나눈 값과 같을 경우 
                return (i+2)**2
            
            elif(i+1 == n): # 자기 자신과는 나눴을 경우 0이므로 자기 자신일 경우 종료해여됨
                return -1
            
            else:
                continue;
                
        else: # 나머지가 0이 아닌경우
            continue
        
print(solution(121))
