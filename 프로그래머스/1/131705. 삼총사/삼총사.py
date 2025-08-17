from itertools import combinations


def solution(number):
    answer = 0
    
    number.sort() # 정렬 
    
    number.index(min(number)) # 최소값을 갖는 인덱스 찾기
    
    for i in combinations(number,3):
        if sum(i) == 0:
            answer+=1
    
    return answer