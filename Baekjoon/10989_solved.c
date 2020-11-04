#include <stdio.h>

int main(void) {
    int N;
    scanf("%d", &N);
    int count[10001] = {0,};
    int i = N;
    int max = 0;
    while (i--) {
        int temp;
        scanf("%d", &temp);
        if (temp > max) {
            max = temp;
        }
        count[temp] += 1;
    }
    for (i = 1; i <= max; i++) {
        int j = count[i];
        while (j--) {
            printf("%d\n", i);
        }
    }
    return 0;
}
