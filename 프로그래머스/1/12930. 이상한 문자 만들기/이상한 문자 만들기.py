def solution(s):
    
    #짝수 인덱스 -> 대문자, 홀수 인덱스 -> 소문자
    
    arr = s.split(' ')
    str_arr = []
    
    print(arr)
    
    for i in arr:
        upper_i = i.upper() # 모두 대문자로 변환
        print(i)
        chr_arr = []
        for j in range(len(upper_i)):
            if j%2 != 0: # 인덱스가 홀수 -> 소문자
                chr_arr.append(upper_i[j].lower()) # 문자열 담기
            else: # 인덱스가 짝수 -> 대문자 그대로 담기
                chr_arr.append(upper_i[j]) 
                
        str_arr.append(''.join(chr_arr))
        
    str_arr = ' '.join(str_arr)        

    return str_arr