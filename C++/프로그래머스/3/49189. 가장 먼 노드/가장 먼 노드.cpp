#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    
    vector<vector<int>> adj(n+1);
    
    // 양방향 간선 만들기
    for (const auto& e: edge){ // 이미 여기서 하나씩 꺼냄
        int u = e[0]; // 3
        int v = e[1]; // 6
        adj[u].push_back(v); // push_back은 노드 연결
        adj[v].push_back(u); 
    }
    
    // 거리 배열 초기회
    vector<int> dist(n+1, -1); // 크기가 n+1이고 모든 값이 -1로 채워짐 노드 1입장에서만
    queue<int> q; // 방문할 노드들의 대기줄 만들기
    
    q.push(1); // 1 삽입
    dist[1] = 0; // 1번에서 1번까지 거리는 0걸음
    
    while(!q.empty()){ // q가 비면 종료 = 탐색 종료
        int cur = q.front(); // 현재 방문한 노드
        q.pop(); // 맨 앞에 제거
        
        for (int next: adj[cur]){ // next는 나에게 걸려있는 노드들
            if (dist[next] == -1){
                dist[next] = dist[cur] + 1;
                
                q.push(next); // 나에게 걸린 노드 넣기
            }
        }
    }
    
    int max_dist = *max_element(dist.begin(), dist.end()); //값 꺼내게
    int answer = count(dist.begin(), dist.end(), max_dist);
    
    return answer;
}