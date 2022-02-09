// J1

#include <iostream>

using namespace std;

int main() {
    const int specialmonth = 2, specialday = 18;
    int month, day;

    cin >> month;
    cin >> day;

    if (month < specialmonth) cout << "Before" << endl;
    else if (month > specialmonth) cout << "After" << endl;
    else {
        if (day < specialday) cout << "Before" << endl;
        else if (day > specialday) cout << "After" << endl;
        else cout << "Special" << endl;
    }
}
