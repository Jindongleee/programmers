def solution(n):
    
    #몇자리인지 세기
    total = 0
    new = str(n)
    for i in range(len(new)):
        if(i == len(new)):
            break
        total = total + int(new[i])

    return total

# sum() 함수는 ()안에 있는 배열 요소를 모두 합해준다.