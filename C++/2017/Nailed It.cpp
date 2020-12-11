// J5

#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> combinations(int* original, int size) {
    
    vector<int> sums;

    for (int a = 0; a < size; a++) {
        for (int b = a + 1; b < size; b++) {
            int sum = original[a] + original[b];
            sums.push_back(sum);
        }
    }

    return sums;
}

int main() 
{
    int n;
    cin >> n;

    int sizes[n];

    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        sizes[i] = tmp;
    }

    vector<int> sums_list = combinations(sizes, n);
    map<int, int> occurences;

    for (int single_sum : sums_list) {
        if (occurences.find(single_sum) == occurences.end()) {
            occurences[single_sum] = count(sums_list.begin(), sums_list.end(), single_sum);
        }
    }

    map<int, int>::iterator it;
    
    vector<int> widths;

    for (it = occurences.begin(); it != occurences.end(); it++) {
        widths.push_back(it->second);
    }

    long max_width = *max_element(widths.begin(), widths.end());
    
    cout << max_width << " " << count(widths.begin(), widths.end(), max_width) << endl;
}