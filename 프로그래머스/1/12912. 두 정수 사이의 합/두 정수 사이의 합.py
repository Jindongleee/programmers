def solution(a, b):
    
    arr = []
    
    if (b-a < 0):
        a, b = b, a
        
    for i in range((b-a)+1):
            arr.append(a+i)
    
    return sum(arr)
            
print(solution(3,5))