#include <algorithm>
#include <cmath>
#include <iostream>
#include <utility>
#include <vector>

int main(int argc, char *argv[]) {
  // take in the number of data inputs
  int numInputs;
  std::cin >> numInputs;

  // to store the data
  std::vector<std::pair<long long, long long>> data;

  // take the number of inputs
  for (int i = 0; i < numInputs; i++) {
    long long time, position;
    std::cin >> time >> position;

    data.push_back(std::make_pair(time, position));
  }

  // sort the data
  std::sort(data.begin(), data.end());

  // to store the max speed
  long double maxSpeed = 0.0;

  for (size_t i = 0; i < data.size() - 1; i++) {
    std::pair<long long, long long> current = data[i], next = data[i + 1];

    // calculate the current speed
    long double speed = (next.second - current.second) /
                        (long double)(next.first - current.first);

    // take the max of the two
    maxSpeed = std::max(maxSpeed, std::abs(speed));
  }

  std::cout << maxSpeed << std::endl;

  return 0;
}
