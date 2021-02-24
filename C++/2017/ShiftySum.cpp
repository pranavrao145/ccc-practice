// J2

#include <iostream>
using namespace std;

int main() {
    int num, times, sum;
    cin >> num;
    cin >> times;
    sum = num;

    for (int i = 0; i < times; i++) {
        num *= 10;
        sum += num;
    }

    cout << sum << endl;
}