// J5 - doesn't work for all

#include <algorithm>
#include <iostream>
#include <vector>

int M, N;
std::vector<std::vector<int>> matrix;
std::vector<std::pair<int, int>> visited;
bool found = false;

void DFS(int d, int a);

std::vector<std::pair<int, int>> factors(int num) {
    std::vector<std::pair<int, int>> final_factors;

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
    std::cin >> M >> N;

  matrix.resize(M);

  for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
      int num;
      std::cin >> num;

      matrix[i].emplace_back(num);
    }
  }

  DFS(1, 1);

  if (found)
    std::cout << "yes" << std::endl;
  else
    std::cout << "no" << std::endl;

  return 0;
}

void DFS(int d, int a) {
  if (d == M && a == N) {
    found = true;
    return;
  }

  std::vector<std::pair<int, int>> facts = factors(matrix[d - 1][a - 1]);

  if (!found) {
    for (auto fact : facts) {
      if (find(visited.begin(), visited.end(), fact) == visited.end()) {
        visited.emplace_back(fact);
        DFS(fact.first, fact.second);
      }
    }
  }
  return;
}
