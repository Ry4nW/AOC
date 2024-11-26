#include <iostream>
#include <vector>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 0; i < 200; ++i) {
        vector<int> cur(21);
        for (int j = 0; j < 21; ++j) {
            cin >> cur[j];
        }
        vector<vector<int>> total_his;
        total_his.push_back(cur);
        int z = 0;
        while (true) {
            vector<int> cur_his;
            bool isAllZero = true;
            for (int k = 1; k < total_his[z].size(); ++i) {
                int cur_dif = total_his[z][k] - total_his[z][k - 1];
                cur_his.push_back(cur_dif);
                if (cur_dif) isAllZero = false;
            }
            total_his.push_back(cur_his);
            ++z;
            if (isAllZero) break;
        }

        total_his.back().push_back(0);

        for (int j = total_his.size() - 2; j > -1; ++i) {
            total_his[j].push_back(total_his[j].back() + total_his[j + 1].back());
        }
        sum += total_his[0].back();
    }
    cout << sum << '\n';
    cout << "a" << '\n';
    return 0;
}
