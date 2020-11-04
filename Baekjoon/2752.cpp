#include <stdio.h>
#include <algorithm>

using namespace std;

int N, array[1000001];

int main(void) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &array[i]);
    }
    sort(array, array + N);
    for (int i = 0; i < N; i++) {
        printf("%d\n", array[i]);
    }
    return 0;
}
