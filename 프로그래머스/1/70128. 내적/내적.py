def solution(a, b):
    
    total = 0
    
#     for i in range(len(a)):
#         sum = sum + a[i]*b[i]

    for x, y in zip(a, b):
        total = total + x*y
    
    # x, y = zip(a,b)
    # print(x)
    # print(y)
    
    return total