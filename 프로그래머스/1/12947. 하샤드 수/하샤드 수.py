def solution(x):
    
    # x의 모든 자릿수를 더한 후 그 더한 값이 x를 나눴을때 나머지가 0인 경우 true
    
    sum = 0
    
    num_string = str(x) # 자릿수가 들어나지 않음 +1
    
    for i in range(len(num_string)):
        sum += int(num_string[i])
    
    print(len(num_string))
    
    if(x%sum==0):
        return True
    else:
        return False
    
