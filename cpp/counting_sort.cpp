#include <iostream>

using namespace std;

int main(void) {
    int count[5] = {0,};
    int array[30] = {4, 4, 2, 3, 4, 5, 4, 1, 2, 2, 4, 2, 3, 4, 1, 2, 3, 4, 2, 2, 1, 3, 4, 5, 4, 2, 3, 1};
    for (int i = 0; i < 30; i++) {
        count[array[i]-1]++;
    }
    for (int i = 0; i < 5; i++) {
        if (count[i] != 0) {
            for (int j = 0; j < count[i]; j++) {
                cout << i + 1 << ' ';
            }
        }
    }
}
