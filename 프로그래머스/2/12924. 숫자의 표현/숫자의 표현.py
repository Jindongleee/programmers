# def solution(n):
    
#     # n값을 만드는 연속된 숫자들의 개수가 result
    
#     # 만약 값이 n보다 크다면 패스
#     # 만약 값이 n보다 부족하다면 
    
#     answer = 0
#     arr = []
    
#     for i in range(1,n+1):
#         arr.append(i)
        

#     # sliding window 개수
#     for i in range(1,n+1): 
        
#         j = 0
#         #마지막 인덱스가끝에 닿았을때 
#         while j+i-1 <= (len(arr)-1):
#             if sum(arr[j:j+i]) == n:
#                 answer+=1
#                 break
#             j+=1
    
#     return answer

def solution(n):
    answer = 0
    for start in range(1, n+1):
        total = 0
        for end in range(start, n+1):
            total += end
            if total == n:
                answer += 1
                break
            elif total > n:
                break
    return answer