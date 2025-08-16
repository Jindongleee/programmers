def solution(s):
    
    answer = s.split(' ')
    
    num_list=[]
    
    length = len(answer)
    
    for i in range(length):
        num_list.append(int(answer[i]))
    
    num_list.sort()
    
    test1 = list(map(int, s.split(' ')))
    print(test1)
    
    test2 = map(int, s.split(' ')) # map -> 원하는 타입으로 쉽게 변경가능
    print(test2)
    
    return str(num_list[0]) + " " + str(num_list[length-1])