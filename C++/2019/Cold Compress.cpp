// J3

#include <iostream>
#include <string>

using namespace std;

int n;
int count = 0;
char character = ' ';

void compress(string line) {
    for (int i = 0; i < line.length(); i++) {
        if (i == 0) {
            character = line[i];
            count = 1;
        }
        else if (i != line.length() - 1) {
            if (line[i] == character) {
                count += 1;
            }
            else {
                cout << count << " " << character << " ";
                character = line[i];
                count = 1;
            }
        }
        else {
            if (line[i] == character) {
                count += 1;
                cout << count << " " << character << endl;
            }
            else {
                cout << count << " " << character << " ";
                character = line[i];
                count = 1;
                cout << count << " " << character << endl;
            }
        }
    }
}

int main() {
    cin >> n;
    string lines[n];
    for (int i = 0; i < n; i++) {
        cin >> lines[i];
    }
    for (int i = 0; i < n; i++) {
        compress(lines[i]);
    }
}