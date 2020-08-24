// J3

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    string consonants, nearestvowel, nearestconsonant, str1, str2 = "";
    consonants = "bcdfghjklmnpqrstvwxyz";
    nearestvowel = "aaeeeiiiiooooouuuuuuu";
    nearestconsonant = "cdfghjklmnpqrstvwxyzz";

    getline(cin, str1);
    
    for (size_t i = 0; i < str1.size(); i++)
    {
        if(find(consonants.begin(), consonants.end(), str1[i]) != str1.end()) {
            int index = consonants.find(str1[i]);
            str2 = str2 + str1[i] + nearestvowel[index] + nearestconsonant[index];
        }
        else str2 += str1[i];
    }
    
    cout << str2 << endl;
    
}