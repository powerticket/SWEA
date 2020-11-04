#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getParent(int parent[], int x) {
    if (parent[x] == x) return x;
    else return parent[x] = getParent(parent, parent[x]);
}

int unionParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int compareParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    return a == b;
}

class Edge {
public:
    int node[2];
    int distance;
    Edge (int a, int b, int distance) {
        this->node[0] = a;
        this->node[1] = b;
        this->distance = distance;
    }
    bool operator <(Edge &edge) {
        return this->distance < edge.distance;
    }
};

int main() {
    int n = 7;
    int m = 11;

    vector<Edge> v;
    v.push_back(Edge(1, 7, 12));
	v.push_back(Edge(1, 4, 28));
	v.push_back(Edge(1, 2, 67));
	v.push_back(Edge(1, 5, 17));
	v.push_back(Edge(2, 4, 24));
	v.push_back(Edge(2, 5, 62));
	v.push_back(Edge(3, 5, 20));
	v.push_back(Edge(3, 6, 37));
	v.push_back(Edge(4, 7, 13));
	v.push_back(Edge(5, 6, 45));
	v.push_back(Edge(5, 7, 73));

    sort(v.begin(), v.end());

    int parent[10];
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    int cnt = 0;
    int result = 0;
    int n1, n2;
    for (int i = 0; i < v.size(); i++) {
        n1 = v[i].node[0];
        n2 = v[i].node[1];
        if (!compareParent(parent, n1, n2)) {
            unionParent(parent, n1, n2);
            result += v[i].distance;
            cnt += 1;
            if (cnt == n - 1) {
                break;
            }
        }
    }
    printf("%d", result);
}
