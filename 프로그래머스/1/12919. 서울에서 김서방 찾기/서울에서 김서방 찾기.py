def solution(seoul):
    answer = ''
    
    #seoul은 길이 1 이상, 1000 이하인 배열입니다.
    #seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
    #"Kim"은 반드시 seoul 안에 포함되어 있습니다.
    
    for i in range(len(seoul)):
        if "Kim" in seoul[i]:
            which=i
    
    return "김서방은 "+str(which)+"에 있다"