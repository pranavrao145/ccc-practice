// J2

#include <iostream>
#include <cmath>

using namespace std;

int h, M;

bool checkHeight(int t)
{
    int a = (-6 * (int)(pow(t, 4) + 0.5)) + (h * (int)(pow(t, 3) + 0.5)) + (2 * (int)(pow(t, 2) + 0.5)) + t;
    if (a <= 0)
        return true;
    return false;
}

int main()
{
    cin >> h;
    cin >> M;

    for (size_t i = 1; i < M + 1; i++)
    {
        if (checkHeight(i))
        {
            cout << "The balloon first touches the ground at hour:\n" << i << endl;
            return 0; 
        }
    }

    cout << "The balloon does not touch the ground in the given time." << endl;
    
}