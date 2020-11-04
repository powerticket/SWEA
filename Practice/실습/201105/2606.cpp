#include <iostream>
#include <vector>
#include <queue>

#define COMPUTERS_NUMBER 101

using namespace std;

int main() {
    int N, M;
    cin>>N>>M;
    vector<int> relation[COMPUTERS_NUMBER];
    int c1, c2;
    for (int i = 0; i < M; i++) {
        cin>>c1>>c2;
        relation[c1].push_back(c2);
        relation[c2].push_back(c1);
    }
    int result = 0;
    int visited[COMPUTERS_NUMBER] = {0,};
    queue<int> q;
    q.push(1);
    visited[1] = 1;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int i = 0; i < relation[v].size(); i++) {
            int w = relation[v][i];
            if (!visited[w]) {
                q.push(w);
                visited[w] = 1;
                result++;
            }
        }
    }
    cout<<result<<'\n';
}
