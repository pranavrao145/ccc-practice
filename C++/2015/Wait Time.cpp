// J4

#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

tuple<char, int> split(string line)
{
    char command;
    int length = line.length(), num;
    if (length == 3)
    {
        command = line.at(0);
        num = (int)line.at(2) - 48;
    }
    else
    {
        command = line.at(0);
        num = stoi(line.substr(2));
    }

    return make_tuple(command, num);
}

int main()
{
    int numcommands, time = 0;
    cin >> numcommands;

    vector<tuple<char, int>> commands;
    vector<int> people;
    map<int, int> temptimes, finaltimes;
    cin.ignore();
    for (int i = 0; i < numcommands; i++)
    {
        string input;
        getline(cin, input);
        commands.push_back(split(input));
    }

    for (tuple<char, int> command : commands)
    {
        char action = get<0>(command);
        int num = get<1>(command);

        if (action == 'R')
        {
            temptimes[num] = time;
            if (find(people.begin(), people.end(), num) == people.end())
            {
                people.push_back(num);
            }
            time += 1;
        }
        else if (action == 'W')
        {
            time += (num - 1);
        }
        else if (action == 'S')
        {
            if (finaltimes.find(num) == finaltimes.end())
            {
                finaltimes[num] = (time - temptimes[num]);
            }
            else
            {
                finaltimes[num] += (time - temptimes[num]);
            }
            temptimes.erase(num);
            time += 1;
        }
    }

    sort(people.begin(), people.end());

    for (int i = 0; i < people.size(); i++)
    {
        int person = people[i];
        if (temptimes.find(person) == temptimes.end())
        {
            cout << to_string(person) << " " << to_string(finaltimes[person]) << endl;
        }
        else
        {
            cout << to_string(person) << " " << to_string(-1) << endl;
        }
    }
}