// J1

#include <iostream>

using namespace std;

int main()
{
    cout << "How many antennas?" << endl;
    int antennas;
    cin >> antennas;

    cout << "How many eyes?" << endl;
    int eyes;
    cin >> eyes;

    if (antennas >= 3 && eyes <= 4)
        cout << "TroyMartian" << endl;

    if (antennas <= 6 && eyes >= 2)
        cout << "VladSaturnian" << endl;

    if (antennas <= 2 && eyes <= 3)
        cout << "GraemeMercurian" << endl;
}