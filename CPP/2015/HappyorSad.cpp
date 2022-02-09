// J2

#include <iostream>
#include <vector>

using namespace std;

int countOccurences(string data, string toSearch) {
    int occurences = 0;
    size_t pos = data.find(toSearch);

    while(pos != string::npos) {
        occurences++;

        pos = data.find(toSearch, pos + toSearch.size());
    }

    return occurences;
}

int main() {
    string input;

    getline(cin, input);

    int happycount, sadcount;

    happycount = countOccurences(input, ":-)");
    sadcount = countOccurences(input, ":-(");

    if (happycount == 0 && sadcount == 0) cout << "none" << endl;
    else if (happycount > sadcount) cout << "happy" << endl;
    else if (happycount < sadcount) cout << "sad" << endl;
    else cout << "unsure" << endl;

        
}