#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int numCasesOpened;
    int banker;

    cin >> numCasesOpened;
    vector<int> amounts = {
            100,
            500,
            1000,
            5000,
            10000,
            25000,
            50000,
            100000,
            500000,
            1000000
    };

    for (size_t i = 0; i < numCasesOpened; i++) {
        int opened;
        cin >> opened;

        amounts[opened - 1] = 0;
    }

    cin >> banker;
    double avg = accumulate(amounts.begin(), amounts.end(), 0.0) / count(amounts.begin(), amounts.end(), 0);

    if (banker > avg) cout << "deal" << endl;
    else cout << "no deal" << endl;
}