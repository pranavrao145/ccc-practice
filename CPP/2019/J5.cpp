#include <bits/stdc++.h>

int findIndex(std::vector<std::string> &vect, std::string str) {
  std::vector<std::string>::iterator it =
      std::find(vect.begin(), vect.end(), str);

  if (it != vect.end())
    return it - vect.begin();

  return -1;
}

// take a string
// get all the possible mutations at this point
// dfs these mutations and attempt to find one that works
// this function must also return the step that was used
std::vector<std::tuple<int, int, std::string>>
find_mutations(std::string str, std::vector<std::string> &src,
               const std::vector<std::string> &dest) {

  std::vector<std::tuple<int, int, std::string>> possible;

  for (int i = 0; i < str.length() + 1; i++) {
    for (int j = i; j < str.length() + 1; j++) {
      std::string sub = str.substr(i, j - i); // get the current substring

      int idx = findIndex(src, sub);

      // if the substring is part of the rules
      if (idx != -1) {
        std::string copy = str;

        possible.emplace_back(
            std::make_tuple(idx, i, copy.replace(i, j - i, dest[idx])));
      }
    }
  }

  return possible;
}

void dfs(const int currentSteps, const int stepsAllowed,
         const std::string currentString, const std::string &destString,
         const std::vector<std::tuple<int, int, std::string>> records,
         std::vector<std::unordered_set<std::string>> &visited,
         std::vector<std::string> &src, const std::vector<std::string> &dest) {
  // base case: if the number of tries is greater than the total allowed,
  // return
  // or if the condition has been reached, print and return
  // else try the next case. if visited, then skip else attempt to dfs it
  if (currentSteps > stepsAllowed)
    return; // we did not succeed

  if (currentSteps == stepsAllowed && currentString == destString) {
    for (auto i : records) {
      std::cout << std::get<0>(i) + 1 << " " << std::get<1>(i) + 1 << " "
                << std::get<2>(i) << std::endl;
    }

    exit(0); // immediately kill the program to prevent further output
  }

  // if it's already visited for this step return
  if (visited[currentSteps].find(currentString) !=
      visited[currentSteps].end()) {
    return;
  }

  // add this string to the visited list for this step
  visited[currentSteps].insert(currentString);

  for (auto tup : find_mutations(currentString, src, dest)) {
    std::vector<std::tuple<int, int, std::string>> cpy = records;
    cpy.push_back(tup);
    dfs(currentSteps + 1, stepsAllowed, std::get<2>(tup), destString, cpy,
        visited, src, dest);
  }
}

int main(int argc, char *argv[]) {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  std::vector<std::string> rulesSrc(3);
  std::vector<std::string> rulesDest(3);

  std::string src, dest;

  int stepsAllowed;

  std::vector<std::tuple<int, int, std::string>> rec;
  std::vector<std::unordered_set<std::string>> visited(
      15); // 15 steps is the most we can do according to the problem

  for (int i = 0; i < 3; i++)
    std::cin >> rulesSrc[i] >> rulesDest[i];

  std::cin >> stepsAllowed >> src >> dest;

  dfs(0, stepsAllowed, src, dest, rec, visited, rulesSrc, rulesDest);
}
