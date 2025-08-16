def solution(s):
    # 문자열의 길이가 4 or 6이고 모두 num이어야 true 아닌 경우 false
    
#     arr = list(s)
    
#     arr.sort()
    
#     if len(s) != 4 and len(s) != 6:
#         return False
    
#     return False if 65<=ord(arr[len(arr)-1]) else True
    if len(s) != 4 and len(s) !=6:
        return False

    return s.isdigit()