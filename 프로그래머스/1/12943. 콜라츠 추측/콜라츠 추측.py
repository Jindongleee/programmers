def solution(num):
    # 모든 수를 1로 만들기 위함
    # Even -> /2, Odd -> *3 + 1 
    
    count=0
    
    while(num != 1):
        if(num % 2 == 0):
            num/=2
        else:
            num  = num * 3 + 1
            
        count = count + 1
        
        if(count == 501):
            return -1
    
    return count