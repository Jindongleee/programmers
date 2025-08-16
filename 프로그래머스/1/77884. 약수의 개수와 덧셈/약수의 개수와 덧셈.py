def solution(left, right):
    
    total = 0
    
    while left <= right :
        count = 0
        
        for i in range(left):
            if(left%(i+1)==0):
                count+=1 #약수의 개수
        
        if (count % 2 == 0):
            total += left
        else:
            total -= left
        
        left+=1
    
    # for i in range(left):
    #     if(left%(i+1)==0):
    #         count+=1
    # print(count)
    
    return total