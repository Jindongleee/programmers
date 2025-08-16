def solution(n):
    
    answer = []
    new = str(n)
    for i in range(len(new)):
        answer.append(int(new[i]))
    
    answer.reverse()
    return answer