// J5 - doesn't work for all

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N;
vector<vector<int>> matrix;
bool found = false;
vector<pair<int, int>> visited;

void DFS(int d, int a);


vector<pair<int, int>> factors(int num) {
    vector<pair<int, int>> final_factors;

    for (int i = 1; i < num + 1; i++) {
        if (num % i == 0) {
            if (i <= M && num / N <= N) {
                final_factors.emplace_back(i, num / i);
            }
        }
    }

    return final_factors;
}

int main() {
    cin >> M;
    cin >> N;

    matrix.resize(M);

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            int num;
            cin >> num;

            matrix[i].push_back(num);
        }
    }

    DFS(1, 1);

    if (found) cout << "yes" << endl;
    else cout << "no" << endl;

    return 0;
}


void DFS(int d, int a) {
    if (d == M && a == N) {
        found = true;
        return;
    }

    vector<pair<int, int>> facts = factors(matrix[d - 1][a - 1]);

    if (!found) {
        for (auto fact : facts) {
            if (find(visited.begin(), visited.end(), fact) == visited.end()) {
                visited.push_back(fact);
                DFS(fact.first, fact.second);
            }
        }
    }
}