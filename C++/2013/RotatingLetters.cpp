// J2

#include <iostream>

using namespace std;

bool is_possible(string word) {
    string letters = "IOSHZXN";

    for (size_t i = 0; i < word.size(); i++)
    {
        if(letters.find(word[i]) == string::npos) return false;
    }
    
    return true;
    

}

int main() {
    string word;

    cin >> word;

    if(is_possible(word)) cout << "YES" << endl;
    else cout << "NO" << endl;
}