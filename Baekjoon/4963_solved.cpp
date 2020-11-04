#include <iostream>
#include <vector>
#include <queue>

#define LIMIT 50

using namespace std;

int dr[8] = {1, -1, 1, -1, 1, -1, 0, 0};
int dc[8] = {-1, 1, 1, -1, 0, 0, 1, -1};

int main() {
    vector<int> result;
    while (true) {
        int w, h;
        cin>>w>>h;
        if (!w and !h) break;
        int map[LIMIT][LIMIT] = {0,};
        int visited[LIMIT][LIMIT] = {0,};
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                int temp;
                cin>>temp;
                map[i][j] = temp;
            }
        }
        int count = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] && !visited[i][j]) {
                    count++;
                    queue<pair<int, int>> q;
                    q.push(pair<int, int>(i, j));
                    visited[i][j] = 1;
                    while (!q.empty()) {
                        int r = q.front().first;
                        int c = q.front().second;
                        q.pop();
                        for (int d = 0; d < 8; d++) {
                            int nr = r + dr[d];
                            int nc = c + dc[d];
                            if (nr >= 0 && nr < h && nc >= 0 && nc < w) {
                                if (map[nr][nc] && !visited[nr][nc]) {
                                    q.push(pair<int, int>(nr, nc));
                                    visited[nr][nc] = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        result.push_back(count);
    }
    for (int i = 0; i < result.size(); i++) {
        cout<<result[i]<<'\n';
    }
    return 0;
}
