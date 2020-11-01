#include <iostream>

using namespace std;

int ans = 0;

void pi(int pieces, int people, int min) {
    if (people == 1) {
        ans++;
        return;
    }

    for (size_t i = min; i < ((pieces / people) + 1); i++)
    {
        pi(pieces - i, people - 1, i);
    }
    
}

int main() {
    int n, k;
    
    cin >> n;
    cin >> k;

    pi(n, k, 1);
    
    cout << ans << endl;
}