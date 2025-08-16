import numpy as np

def solution(arr1, arr2):
    
    col = len(arr1) # 열
    row = len(arr1[0]) #행
    answer = []
    
    for i in range(col):
        arr = []
        for j in range(row):
            arr.append(arr1[i][j]+arr2[i][j])
        answer.append(arr)
    
    return answer

    # A = np.array(arr1)
    # B = np.array(arr2)
    # C = A+B
    
