#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    int array[10] = {10, 2, 3, 6, 5, 4, 7, 9, 1, 8};
    sort(array, array+10, greater<>());
    for (int i = 0; i < 10; i++) {
        cout << array[i] << " ";
    }
    return 0;
}