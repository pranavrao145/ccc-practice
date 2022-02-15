#include <cstring>
#include <iostream>

int main(int argc, char *argv[]) {
  int M, N, K, counter = 0;

  // take input
  std::cin >> M;
  std::cin >> N;
  std::cin >> K;

  int *rows = new int[M];
  int *cols = new int[N];

  std::memset(rows, 0, M * sizeof(int));
  std::memset(cols, 0, N * sizeof(int));

  for (int i = 0; i < K; i++) {
    char ins;
    int num;

    std::cin >> ins;
    std::cin >> num;

    if (ins == 'R')
      rows[num - 1] = !rows[num - 1];
    else if (ins == 'C')
      cols[num - 1] = !cols[num - 1];
  }

  // iterate to figure out how many golds there are
  for (int i = 0; i < M; i++) {
    int isChecked = rows[i];
    for (int j = 0; j < N; j++) {
      if (isChecked != cols[j])
        counter++;
    }
  }

  std::cout << counter << std::endl;

  return 0;
}
