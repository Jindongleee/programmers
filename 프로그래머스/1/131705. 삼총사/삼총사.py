from itertools import combinations


def solution(number):
    answer = 0
    
    number.sort() # 정렬 
    
    number.index(min(number)) # 최소값을 갖는 인덱스 찾기
    
    # 1번 방법 -> combinations를 통해 3개의 부분집합 모두 찾기
    # for i in combinations(number,3):
    #     if sum(i) == 0:
    #         answer+=1

    # 2번 방법 3중 포인터
    
    if len(number) >= 0:
        for i in range(len(number)-2):
            for j in range(i+1,len(number)-1):
                for k in range(j+1, len(number)):
                    if (number[i]+number[j]+number[k]) == 0:
                        answer+=1
    else:
        print("Don't enough length")
    
    return answer