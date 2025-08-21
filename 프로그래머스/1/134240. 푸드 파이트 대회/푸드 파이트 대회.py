def solution(food):
    
    # 왼쪽에서 시작하는 선수와 오른쪽에서 시작하는 선수가 중간에서 물을 먼저 먹는 사람이 우승
    # 인덱스 0 -> 물 1개 의미 1,3,4,6 -> 물 1개 1번음식 3개 2번음식 4개 3번음식 6개
    # 짝수개로 맞춰서 준비
    arr = []
    dic= dict()
    
    for i in range(1, len(food)):
        if food[i]//2 >=1:# 몫이 1보다 커야 분배가 가능하므로
            dic[i]=(food[i]//2)
            
    for key, value in dic.items():
        arr.append(str(key)*value)
    
    answer = ''.join(arr)
    
    return answer + '0' + answer[::-1]