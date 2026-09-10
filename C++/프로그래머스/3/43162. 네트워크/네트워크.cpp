#include <string>
#include <vector>

using namespace std;

// 연결이 되어있으면 하나인거고, 아니면 개별인거고
// 최대 n개인데, 만약 연결되어있는게 있다면 -1씩 추가,
vector<bool> visited;

// dfs 를 통해 true로 바꾸기
void dfs(int cur, int n, vector<vector<int>> computers){
    visited[cur] = true;  // 방문 한거니까 true
    for (int i = 0; i<n; i++){ // 
        if(computers[cur][i] == 1 && !visited[i])
            dfs(i, n, computers);
    }    
}
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    visited.assign(n, false); // 모든 노드들 방문 안했다고 가정
  
    for (int i=0;i<n;i++){
        if (!visited[i]){ // 방문 한적이 없는 애다? 그러면 바로 전수조사
            dfs(i, n, computers); // dfs를 통해 연결되어있는 애들 전부 visited true 바꾸기 = 연결되어있다는 뜻이니까
            answer ++;
        }
    }
    
    return answer;
}