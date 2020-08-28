// J2

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int chore_count = 0, sum_chore_times = 0, max_time, chores;
    vector<int> chore_times;

    cin >> max_time;
    cin >> chores;

    // get input
    for (size_t i = 0; i < chores; i++)
    {
        int num;
        cin >> num;
        chore_times.push_back(num);
    }

    // filter input if bigger than max time
    for (size_t i = 0; i < chore_times.size(); i++)
    {
        if(chore_times[i] > max_time) chore_times.erase(chore_times.begin() + i);
    }

    sort(chore_times.begin(), chore_times.end());

    for (size_t i = 0; i < chore_times.size(); i++)
    {
        sum_chore_times += chore_times[i];
        if (sum_chore_times <= max_time)
        {
            chore_count++;
        }
        
    }

    cout << chore_count << endl;
        

    
    
}