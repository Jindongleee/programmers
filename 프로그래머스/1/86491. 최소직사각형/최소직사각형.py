def solution(sizes):
    
    # 1. sizes에서 가장 큰 값을 찾은 후 각 명함 번호에서 sizes에 가장 가까운 값을 제거 한다.
    # 2. 이후 sizes배열에서 남은 값들의 최대 값을 구해서 
    # 3. 1번과 2번의 곲 -> 최소값
    max_arr = []
    min_arr = []
    for i in sizes:
        if i[0] >= i[1]:
            max_arr.append(i[0])
            min_arr.append(i[1])
        else:
            max_arr.append(i[1])
            min_arr.append(i[0])
    
    return max(max_arr) * max(min_arr)