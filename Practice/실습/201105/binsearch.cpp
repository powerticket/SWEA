#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int binSearch(vector<int> array, int compare, int start, int end, int direction);

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        int result = 0;
        int N, M;
        cin>>N>>M;
        vector<int> reference;
        vector<int> compare;
        for (int i = 0; i < N; i++) {
            int temp;
            cin>>temp;
            reference.push_back(temp);
        }
        for (int i = 0; i < M; i++) {
            int temp;
            cin>>temp;
            compare.push_back(temp);
        }
        sort(reference.begin(), reference.end());
        for (int i = 0; i < M; i++) {
            int b = binSearch(reference, compare[i], 0, N-1, 0);
            result += b;
        }        
        cout<<'#'<<t<<' '<<result<<'\n';
    }
    return 0;
}

int binSearch(vector<int> array, int compare, int start, int end, int direction) {
    if (start > end) return 0;
    int result = 0;
    int mid = (start + end) / 2;
    if (compare == array[mid]) return 1;
    else if (compare > array[mid]) {
        if (direction != 1) result = binSearch(array, compare, mid + 1, end, 1);
        else return 0;
    } else {
        if (direction != -1) result = binSearch(array, compare, start, mid - 1, -1);
        else return 0;
    }
    return result;
}
