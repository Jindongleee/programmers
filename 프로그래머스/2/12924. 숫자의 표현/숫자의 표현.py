import itertools

# 방법 1
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

# --------------------------------------- 성능 최악

# 방법 2

# def solution(n):
#     answer = 0
#     for start in range(1, n+1):
#         total = 0
#         for end in range(start, n+1):
#             total += end
#             if total == n:
#                 answer += 1
#                 break
#             elif total > n:
#                 break
#     return answer

# ---------------------------- 최적

# 방법 3
# 1. 연속성 확인하는 함수 제작
# 2. combinations를 통해 합 확인 후 그것이 연속성이 있다 -> 카운트 
#def check_consequence(arr):
    
#     length = len(arr)
    
#     for i in range(length):
#         if i+1 < length: # index out of range 방지
#             if (arr[i] + 1) == arr[i+1]:
#                 continue
#             else:
#                 return False
#         else:
#             return True
#    return all(arr[i] + 1 == arr[i+1] for i in range(len(arr)-1)) # 위를 축약

# def solution(n):
    
#     arr = list(range(1,n+1)) # n을 통한 리스트 생성
#     print(arr)
    
#     count = 0
    
#     for i in range(1,n+1):
#         for j in itertools.combinations(arr,i):  # 조합은 부분집합 모두 탐색 -> 2^n 수준 복잡도
#             if sum(j) == n and check_consequence(j):
#                 count+=1

#     return count

def solution(n):
    count = 0
    k = 1
    while k * (k+1) // 2 <= n:  # 최소 합이 n을 넘지 않을 때까지만
        if (n - k*(k-1)//2) % k == 0:
            count += 1
        k += 1
    return count


    