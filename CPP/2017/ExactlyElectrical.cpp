// J3

#include <iostream>
#include <cmath>
using namespace std;


int main() {
    int charge, pointA[2], pointB[2];

    for(int i = 0; i < 2; i++) {
        cin >> pointA[i];
    } 
    for(int i = 0; i < 2; i++) {
        cin >> pointB[i];
    }

    cin >> charge;

    int distance = abs(pointA[0] - pointB[0]) + abs(pointA[1] + pointB[1]);

    if (distance % 2 == charge % 2) cout << 'Y'; else cout << 'N';
    
    cout << endl;

}