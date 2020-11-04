#include <iostream>
#include <algorithm>

using namespace std;

string str[20000];
int N;

int getSum(string a) {
    int length = a.length(), sum = 0;
    for (int i = 0; i < length; i++) {
        if (a[i] - '0' <= 9 && a[i] - '0' >= 0) {
            sum += a[i] - '0';

        }
    }
    return sum;
}

bool cmp (string a, string b) {
    if (a.length() != b.length()) {
        return a.length() < b.length();
    }
    int aSum = getSum(a), bSum = getSum(b);
    if (aSum != bSum) {
        return aSum < bSum;
    }
    return a < b;
}

int main(void) {
    cin >> N;
    int i = N;
    while (i--) {
        cin >> str[i];
    }
    sort(str, str+N, cmp);
    for (i = 0; i < N; i++) {
        cout << str[i] << '\n';
    }
    return 0;
}
