def solution(phone_number):
    
#     str = []
    
#     for i in range(len(phone_number)-4):
#         str.append("*")
    
#     for i in range(4):
#         str.append(phone_number[len(phone_number)-4+i])
        
#     str = ''.join(str)
#     return str

    str = "*"*(len(phone_number)-4)+phone_number[len(phone_number)-4:]
    return str
    