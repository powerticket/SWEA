#include <iostream>
#include <vector>
#include <queue>

#define FRIENDS 501

using namespace std;

int main(int argc, char** argv) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, M;
        cin >> N >> M;
        int start, end;
        vector<int> G[FRIENDS];
        for (int i = 0; i < M; i++) {
            cin >> start >> end;
            G[start].push_back(end);
            G[end].push_back(start);
        }
        int result = 0;
        queue<int> q;
        int check[FRIENDS] = {0,};
        q.push(1);
        check[1] = 1;
        int v;
        while (!q.empty()) {
            v = q.front();
            q.pop();
            if (check[v] > 3) {
                break;
            }
            for (int i = 0; i < G[v].size(); i++) {
                int w = G[v][i];
                if (!check[w]) {
                    q.push(w);
                    check[w] = check[v] + 1;
                    if (check[w] < 4) {
                        result++;
                    }
                }
            }
        }
        cout << '#' << t << ' ' << result << '\n';
    }
    return 0;
}
