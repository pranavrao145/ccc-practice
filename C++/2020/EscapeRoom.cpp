#include <iostream>
#include <algorithm>
#include <vector>
#include <tuple>

using namespace std;

int down, across;

vector<tuple<int, int>> factors(int number) {
    vector<tuple<int, int>> factors;

    for(size_t i=1; i < number + 1; i++) {
        if (number % i == 0) {
            if (i <= down && number / i <= across) {
                factors.push_back(new tuple<int, int>(i, number / i));
            } 
        }
    }
}

int main() {
    
}