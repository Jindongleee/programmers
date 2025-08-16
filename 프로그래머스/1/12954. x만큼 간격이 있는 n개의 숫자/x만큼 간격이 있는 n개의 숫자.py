def solution(x, n):
    # x 초기값
    # x ~ n*x 등차 수열 적용된 공차는 x 배열 반환
    # an = a1+(n-1)d
    # 삽입, 삭제, 추가
    arr = []
    
    for i in range(n):
        arr.append(x+(i)*x)
    
    return arr


print(solution(2,5))