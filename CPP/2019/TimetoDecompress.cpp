// J2

#include <iostream>
using namespace std;

int main()
{
    int numlines;

    cin >> numlines;

    int numbers[numlines];
    char characters[numlines];

    for(int i = 0; i < numlines; i++) {
        cin >> numbers[i];
        cin >> characters[i];
    }
    for(int i =0; i < numlines; i++) {
        string str(numbers[i], characters[i]);
        cout << str << endl;
    }
}