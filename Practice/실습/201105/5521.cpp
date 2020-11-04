#include <iostream>
#include <vector>
#include <queue>

#define FRIENDS 501

using namespace std;

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        int N, M;
        cin>>N>>M;
        int a, b;
        vector<int> relation[FRIENDS];
        for (int i = 0; i < M; i++) {
            cin>>a>>b;
            relation[a].push_back(b);
            relation[b].push_back(a);
        }
        int count = 0;
        int visited[FRIENDS] = {0,};
        queue<int> q;
        q.push(1);
        visited[1] = 1;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            if (visited[v] > 3) {
                break;
            }
            for (int i = 0; i < relation[v].size(); i++) {
                int w = relation[v][i];
                if (!visited[w]) {
                    q.push(w);
                    visited[w] = visited[v] + 1;
                    if (visited[w] < 4) {
                        count++;
                    }
                }
            }
        }
        cout<<'#'<<t<<' '<<count<<'\n';
    }
    return 0;
}
