// J4

#include <iostream>
#include <algorithm>
using namespace std;

int row1[] = {1, 2};
int row2[] = {3, 4};

void hflip() {
    swap(row1[0], row2[0]);
    swap(row1[1], row2[1]);
}

void vflip() {
    swap(row1[0], row1[1]);
    swap(row2[0], row2[1]);
}

int main() {
    string sequence;

    cin >> sequence;

    for (int i = 0; i < sequence.size(); i++) {
        if (sequence[i] == 'H') hflip(); else vflip();
    }

    cout << row1[0] << ' ' << row1[1] << endl;
    cout << row2[0] << ' ' << row2[1] << endl;

}