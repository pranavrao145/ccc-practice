// J3

#include <iostream>
#include <algorithm>

using namespace std;

bool check(int y)
{
    string year = to_string(y);

    for (size_t i = 0; i < year.length(); i++)
    {
        if (count(year.begin(), year.end(), year[i]) > 1) return false;
    }

    return true;
}

int main() {
    int year;
    cin >> year;
    year++;
    while (!check(year))
    {
        year++;
    }

    cout << year << endl;
}