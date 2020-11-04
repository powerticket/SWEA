#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;
int N;
string str[20000];

bool compare(string a, string b) {
    if (a.size() == b.size()) {
        return a < b;
    }
    return a.size() < b.size();
}

int main(void) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        cin >> str[i];
    }
    sort(str, str+N, compare);
    for (int i = 0; i < N; i++) {
        if (i > 0 && str[i] == str[i-1]) {
            continue;
        } else {
            printf("%s\n", str[i].c_str());
        }
    }
    return 0;
}
