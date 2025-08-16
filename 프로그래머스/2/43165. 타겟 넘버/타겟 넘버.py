def solution(numbers, target):
    # target = +, - 을 통해 목표를 하는 수
    # numbers 는 숫자 배열 (바뀌지 않음) -> 이를 +, - 하여 target의 수를 만들어라

    # 1. target을 root 노드로 시작하여 +4, -4 를 모두 순회
    def dfs(index, goal):
        if(index == len(numbers)): # 종료 시점
            if(goal == 0):
                return 1;
            else:
                return 0;
        plus = dfs(index + 1, goal + numbers[index])
        minus = dfs(index + 1, goal - numbers[index])
        
        return plus + minus

    return dfs(0,target)
    
