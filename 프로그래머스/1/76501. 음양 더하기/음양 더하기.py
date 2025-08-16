def solution(absolutes, signs):
    
    # signs에 대응대는 absolutes 실제 값을 더해라
    
    arr = []
    
    for i in range(len(signs)):
        if(signs[i]==True):
            arr.append(absolutes[i])
        else:
            arr.append(-absolutes[i])
            
    return sum(arr)
