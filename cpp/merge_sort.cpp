#include <stdio.h>

int number = 10;
int sorted_array[10];

void merge(int a[], int m, int middle, int n) {
    int i = m;
    int j = middle + 1;
    int k = m;
    while (i <= middle && j <= n) {
        if (a[i] <= a[j]) {
            sorted_array[k] = a[i];
            i++;
        } else {
            sorted_array[k] = a[j];
            j++;
        }
        k++;
    }
    if (i > middle) {
        for (int t = j; t <= n; t++) {
            sorted_array[k] = a[t];
            k++;
        }
    } else {
        for (int t = i; t <= middle; t++) {
            sorted_array[k] = a[t];
            k++;
        }
    }
    for (int t = m; t <= n; t++) {
        a[t] = sorted_array[t];
    }
}

void mergeSort(int a[], int m, int n) {
    if (m < n) {
        int middle = (m + n) / 2;
        mergeSort(a, m, middle);
        mergeSort(a, middle + 1, n);
        merge(a, m, middle, n);
    }
}

int main(void) {
    int array[number] = {7, 6, 5, 8, 3, 5, 9, 1, 10};
    mergeSort(array, 0, number - 1);
    for (int i = 0; i < number; i++) {
        printf("%d\n", array[i]);
    }
    return 0;
}