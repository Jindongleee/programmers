def solution(s):
    answer = ''
    
    arr = []
    arr2 = []
    
#     for i in range(len(s)):
#         arr.append(ord(s[i]))
    
#     arr.sort(reverse=True)
    
#     for i in range(len(s)):
#         arr2.append(chr(arr[i]))
    
    print(list(s))
    arr = list(s)
    arr.sort(reverse=True)
    print(arr)
        
    return ''.join(arr)