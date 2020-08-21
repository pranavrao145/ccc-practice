// J4

#include <iostream>
using namespace std;

int numDigits(int x){
    return to_string(x).length();
}

bool threeDigitCheck(int t) {
    string time = to_string(t);
    int x = (int)time[0] - 48;
    int y = (int)time[1] - 48;
    int z = (int)time[2] - 48;

    if (x + 1 == y && y + 1 == z) return true;

    return false;

}


bool fourDigitCheck(int t) {
    string time = to_string(t);
    int w = (int)time[0] - 48;
    int x = (int)time[1] - 48;
    int y = (int)time[2] - 48;
    int z = (int)time[3] - 48;

    if (w + 1 == x && x + 1 == y && y + 1 == z) return true;

    return false;

}


int main() {
    int minutes, count = 0, time=1200;

    cin >> minutes;

    for (int i = 0; i < minutes; i++) {
        time += 1;
        if (time == 1260) {
            time = 100;
        }
        for (int a = 1; a < 12; a++) {
            if (time == (a * 100) + 60) {
                time = (a + 1) * 100;
            }
            else {
                continue;
            }
        }
        if (numDigits(time) == 3) {
             if (threeDigitCheck(time)) count += 1;
        }
        else {
            if (fourDigitCheck(time)) count += 1;
        }
    }

    cout << count << endl;
}