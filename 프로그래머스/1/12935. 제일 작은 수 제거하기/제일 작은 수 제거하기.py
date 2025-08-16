def solution(arr):
    
    m = min(arr)
    i = arr.index(m)
    print(m)    
    print(i)
    
    del arr[i]
    
    if(len(arr) == 0):
        return [-1]
    
    return arr
    
    #return arr[:-1] if (len(arr[:-1]) != 0) else [-1]

arr=[3,2,1,4]

arr.sort()

arr.reverse()
print(arr)