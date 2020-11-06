#include <iostream>
#include <queue>

using namespace std;

int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin>>N;
        int map[100][100] = {0,};
        int cost[100][100] = {0,};
        for (int i = 0; i < N; i++) {
            string temp;
            cin>>temp;
            for (int j = 0; j < N; j++) {
                map[i][j] = temp[j] - '0';
                cost[i][j] = 10000000;
            }
        }
        queue<int> qr;
        queue<int> qc;
        qr.push(0);
        qc.push(0);
        cost[0][0] = 0;
        while (!qr.empty()) {
            int r = qr.front();
            int c = qc.front();
            qr.pop();
            qc.pop();
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                    if (cost[nr][nc] > cost[r][c] + map[nr][nc]) {
                        qr.push(nr);
                        qc.push(nc);
                        cost[nr][nc] = cost[r][c] + map[nr][nc];
                    }
                }
            }
        }
        cout<<'#'<<t<<' '<<cost[N-1][N-1]<<'\n';
    }
    return 0;
}
