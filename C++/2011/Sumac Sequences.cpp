// J3

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int term1, term2, flag = 0, prevtermindex = 0, currenttermindex = 1;

    vector<int> sequences;

    cin >> term1;
    cin >> term2;

    sequences.push_back(term1);
    sequences.push_back(term2);


    while (flag == 0)
    {
        int a = sequences[prevtermindex] - sequences[currenttermindex];

        sequences.push_back(a);

        if (a > sequences[currenttermindex])
        {
            flag = 1;
        }

        prevtermindex++;
        currenttermindex++;
    }

    cout << sequences.size() << endl;
}