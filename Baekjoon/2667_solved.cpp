#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int dr[4] = {1, -1, 0, 0};
int dc[4] = {0, 0, 1, -1};

int main() {
    int N;
    cin>>N;
    vector<string> square;
    for (int i = 0; i < N; i++) {
        string temp;
        cin>>temp;
        square.push_back(temp);
    }
    int result = 0;
    vector<int> house;
    int visited[25][25] = {0,};
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (square[i][j] == '1' && !visited[i][j]) {
                int count = 1;
                result++;
                queue<int> row;
                queue<int> column;
                row.push(i);
                column.push(j);
                visited[i][j] = 1;
                while (!row.empty()) {
                    int r = row.front();
                    int c = column.front();
                    row.pop();
                    column.pop();
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                            if (square[nr][nc] == '1' && !visited[nr][nc]) {
                                row.push(nr);
                                column.push(nc);
                                visited[nr][nc] = 1;
                                count++;
                            }
                        }
                    }
                }
                house.push_back(count);
            }
        }
    }
    sort(house.begin(), house.end());
    cout<<result<<'\n';
    for (int i = 0; i < house.size(); i++) {
        cout<<house[i]<<'\n';
    }
    return 0;
}
