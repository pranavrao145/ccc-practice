#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string shelf;
    cin >> shelf;

    int numl = count(shelf.begin(), shelf.end(), 'L');
    int numm = count(shelf.begin(), shelf.end(), 'M');
    int nums = count(shelf.begin(), shelf.end(), 'S');

    string l_section = shelf.substr(0, numl);
    string m_section = shelf.substr(numl, numm);
    string s_section = shelf.substr(numl + numm);

    int lm_section_displaced_max = max(count(l_section.begin(), l_section.end(), 'M'), count(m_section.begin(), m_section.end(), 'L'));
    int s_section_displaced = s_section.length() - count(s_section.begin(), s_section.end(), 'S');

    cout << lm_section_displaced_max + s_section_displaced << endl;
}
