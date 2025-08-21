import itertools

def solution(numbers):
    answer = []
    
    for i in itertools.combinations(numbers,2):
        answer.append(sum(i))
    
    answer = list(set(answer))
    
    answer.sort()
    return answer