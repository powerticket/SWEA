#include <stdio.h>

int getParent(int parent[], int x) {
    if (parent[x] == x) return x;
    return parent[x] = getParent(parent, parent[x]);
}

int main() {
    int parent[5] = {0, 0, 1, 2, 3};
    // for (int i = 0; i < 5; i++) {
    //     printf("%d ", parent[i]);
    // }
    // printf("\n");
    // for (int i = 0; i < 5; i++) {
    //     printf("%d ", getParent(parent, i));
    // }
    // printf("\n");
    // for (int i = 0; i < 5; i++) {
    //     printf("%d ", parent[i]);
    // }
    printf("%d\n", parent[4]);
    printf("%d\n", getParent(parent, 4));
    printf("%d\n", parent[4]);
}