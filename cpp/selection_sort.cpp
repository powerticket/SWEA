#include <iostream>

using namespace std;

int main(void) {
	int i, j, min, index, temp;
	int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for (i = 0; i < 10; i++) {
		min = 9999;
		for (j = i; j < 10; j++) {
			if (array[j] < min) {
				min = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;		
	}
	for (i = 0; i < 10; i++) {
		cout << array[i] << endl;
	}
	return 0;
}
