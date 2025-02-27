import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int minAbs = Integer.MAX_VALUE;

        // 그래프(트리) 생성
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            
            // 1~송전탑 개수 (노드 개수 만큼) , ArrayList 객체로 초기화
            graph.put(i, new ArrayList<>());  
            
        }
        
        // 모든 그래프 노드에 자식노드 존재 -> 추가
        // 무방향 그래프
        for (int[] wire : wires) {
            graph.get(wire[0]).add(wire[1]);
            graph.get(wire[1]).add(wire[0]);
        }

        // 모든 간선을 하나씩 제거하며 탐색
        for (int[] wire : wires) {
            int v1 = wire[0], v2 = wire[1];

            // DFS 탐색으로 한쪽 서브트리의 크기 계산
            int treeSize = dfs(graph, n, v1, v2);
            int otherTreeSize = n - treeSize;

            // 최소 차이 갱신
            minAbs = Math.min(minAbs, Math.abs(treeSize - otherTreeSize));
        }
        return minAbs;
    }

    // graph , 노드 총개수, 시작 노드, 방문 여부 삭제
    private int dfs(Map<Integer, List<Integer>> graph, int n, int start, int removed) {
        Stack<Integer> stack = new Stack<>();
        
        // 
        boolean[] visited = new boolean[n + 1];  // 방문 여부 체크
        stack.push(start);
        visited[start] = true;
        int count = 1;

        while (!stack.isEmpty()) {
            int node = stack.pop();
            
            // ArrayList가 neighbor 
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor] && neighbor != removed) {
                    visited[neighbor] = true;
                    stack.push(neighbor);
                    count++;
                }
            }
        }
        return count;
    }
}