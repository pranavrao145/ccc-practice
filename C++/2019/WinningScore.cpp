// J1

#include <iostream>
using namespace std;

int main() {
    int apoints[3], bpoints[3];

    for (int a=0; a < 3; a++) {
        cin >> apoints[a];
    }

    for (int a=0; a < 3; a++) {
        cin >> bpoints[a];
    }
    
    int ascore = apoints[0] * 3 + apoints[1] * 2 + apoints[2];
    int bscore = bpoints[0] * 3 + bpoints[1] * 2 + bpoints[2];

    if (ascore > bscore) {
        cout << "A" << endl;
    }
    else if (bscore > ascore) {
        cout << "B" << endl;
    }
    else {
        cout << "T" << endl;
    }
}
