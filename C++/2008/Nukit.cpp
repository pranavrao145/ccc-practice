// J5 - to be tested

#include <iostream>
#include <array>

using namespace std;


bool canDoAABDD(int a, int b, int c, int d)
{
    return (a >= 2 && b >= 1 && d >= 2);
}

bool canDoABCD(int a, int b, int c, int d)
{
    return (a >= 1 && b >= 1 && c >= 1 && d >= 1);
}

bool canDoCCD(int a, int b, int c, int d)
{
    return (c >= 2 && d >= 1);
}

bool canDoBBB(int a, int b, int c, int d)
{
    return (b >= 3);
}

bool canDoAD(int a, int b, int c, int d)
{
    return (a >= 1 && d >= 1);
}

bool canMove(int a, int b, int c, int d)
{
    return (canDoAABDD(a, b, c, d) || canDoABCD(a, b, c, d) || canDoCCD(a, b, c, d) || canDoBBB(a, b, c, d) || canDoAD(a, b, c, d));
}

bool isWinningCombo(int, int, int, int);

bool isLosingCombo(int a, int b, int c, int d) {
    if (!canMove(a, b, c, d)) return true;
    else {
        bool temp = true;

        if (canDoAABDD(a, b, c , d)) temp = (temp && isWinningCombo(a - 2, b - 1, c, d - 2));
        if (canDoABCD(a, b, c , d)) temp = (temp && isWinningCombo(a - 1, b - 1, c - 1, d - 1));
        if (canDoCCD(a, b, c , d)) temp = (temp && isWinningCombo(a, b, c - 2, d - 1));
        if (canDoBBB(a, b, c , d)) temp = (temp && isWinningCombo(a, b - 3, c, d));
        if (canDoAD(a, b, c , d)) temp = (temp && isWinningCombo(a - 1, b, c, d - 1));

        return temp;

    }
}

bool isWinningCombo(int a, int b, int c, int d) {
    if (canDoAABDD(a, b, c, d) && isLosingCombo(a - 2, b - 1, c, d - 2)) return true;
    else if (canDoABCD(a, b, c, d) && isLosingCombo(a - 1, b - 1, c - 1, d - 1)) return true;
    else if (canDoCCD(a, b, c, d) && isLosingCombo(a, b, c - 2, d - 1)) return true;
    else if (canDoBBB(a, b, c, d) && isLosingCombo(a, b - 3, c, d)) return true;
    else if (canDoAD(a, b, c, d) && isLosingCombo(a - 1, b, c, d - 1)) return true;
    else return false;
}

int main() {
    int n;

    cin >> n;
    

    for (int i = 0; i < n; i++) {

        int nums[4];
        
        for (int a = 0; a < 4; a++) {
            cin >> nums[i];
        }

        if (isWinningCombo(nums[0], nums[1], nums[2], nums[3])) cout << "Patrick" << endl;
        else cout << "Roland" << endl;

    }
}