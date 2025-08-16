def solution(t, p):
    # t를 p의 길이만큼 자르고 p와 크기 비교를 하여 작은 것을 카운팅
    
    arr=[]
    
    length = len(t[:len(p)])
    i=0
    while(length==len(p)):
        arr.append(t[i:len(p)+i])
        i+=1
        length = len(t[i:len(p)+i])
    
    print(arr)
    
    # 숫자 비교 하기
    count = 0
    for i in arr:
        if (i[0] == '0'):
            i.replace('0','')
        if int(p) >= int(i):
            count+=1
    
    return count