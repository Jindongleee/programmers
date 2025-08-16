def solution(price, money, count):
    
    # 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
    # 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
    # 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
    # money를 넘어가자마자 부족금액 리턴
    
    for i in range(count):
        money -= (price * (i+1))
    
    if(money>=0):
        return 0
    else:
        return abs(money)
