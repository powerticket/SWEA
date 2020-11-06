#include <iostream>
#include <queue>

using namespace std;

int main(int argc, char** argv) {
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        int result = 1;
        int N, M, R, C, L;
        int map[50][50] = {0,};
        int visited[50][50] = {0,};
        cin>>N>>M>>R>>C>>L;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin>>map[i][j];
            }
        }
        queue<int> qr;
        queue<int> qc;
        qr.push(R);
        qc.push(C);
        visited[R][C] = 1;
        int cycle = 1;
        while (cycle < L) {
            int timer = qr.size();
            for (int time = 0; time < timer; time++) {
                int r = qr.front();
                int c = qc.front();
                qr.pop();
                qc.pop();
                int temp = map[r][c];
                bool up = true, down = true, right = true, left = true;
                switch (temp)
                {
                case 2:
                    left = right = false;
                    break;
                case 3:
                    up = down = false;
                    break;
                case 4:
                    left = down = false;
                    break;
                case 5:
                    left = up = false;
                    break;
                case 6:
                    up = right = false;
                    break;
                case 7:
                    down = right = false;
                    break;                
                default:
                    break;
                }
                if (r + 1 < N && !visited[r+1][c] && down) {
                    int temp = map[r+1][c];
                    switch (temp)
                    {
                    case 0:
                        break;
                    case 3:
                        break;
                    case 5:
                        break;
                    case 6:
                        break;                
                    default:
                        qr.push(r+1);
                        qc.push(c);
                        visited[r+1][c] = 1;
                        result++;
                        break;
                    }
                }
                if (r - 1 >= 0 && !visited[r-1][c] && up) {
                    int temp = map[r-1][c];
                    switch (temp)
                    {
                    case 0:
                        break;
                    case 3:
                        break;
                    case 5:
                        break;
                    case 7:
                        break;                
                    default:
                        qr.push(r-1);
                        qc.push(c);
                        visited[r-1][c] = 1;
                        result++;
                        break;
                    }

                }
                if (c + 1 < M && !visited[r][c+1] && right) {
                    int temp = map[r][c+1];
                    switch (temp)
                    {
                    case 0:
                        break;
                    case 2:
                        break;
                    case 4:
                        break;
                    case 5:
                        break;                
                    default:
                        qr.push(r);
                        qc.push(c+1);
                        visited[r][c+1] = 1;
                        result++;
                        break;
                    }

                }
                if (c - 1 >= 0 && !visited[r][c-1] && left) {
                    int temp = map[r][c-1];
                    switch (temp)
                    {
                    case 0:
                        break;
                    case 2:
                        break;
                    case 6:
                        break;
                    case 7:
                        break;                
                    default:
                        qr.push(r);
                        qc.push(c-1);
                        visited[r][c-1] = 1;
                        result++;
                        break;
                    }
                }
            }
            cycle++;
        }
        cout<<'#'<<t<<' '<<result<<'\n';
    }
    return 0;
}
