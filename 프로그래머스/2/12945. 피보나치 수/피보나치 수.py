def solution(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a + b) % 1234567  # 중간에 나머지 연산 적용하여 overflow 방지
    return b