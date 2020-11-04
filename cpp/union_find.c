#include <stdio.h>

int getParent(int parent[], int x) {
    if (parent[x] == x) return x;
    return parent[x] = getParent(parent, parent[x]);
}

int unionParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int findParent(int parent[], int a, int b) {
    a = getParent(parent, a);
    b = getParent(parent, b);
    return a == b;
}

int main() {
    int parent[11];
    for (int i = 0; i < 11; i++) {
        parent[i] = i;
    }
    unionParent(parent, 1, 2);
    unionParent(parent, 2, 3);
    unionParent(parent, 4, 5);
    unionParent(parent, 5, 6);
    unionParent(parent, 6, 7);
    for (int i = 0; i < 11; i++) {
        printf("%d\n", getParent(parent, i));
    }
    for (int i = 2; i < 11; i++) {
        printf("%d and %d are connected? %d\n", 1, i, findParent(parent, 1, i));
    }
}