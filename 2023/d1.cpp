// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     ifstream input;
//     input.open("input.txt");
//     vector<string> lines(1000);
//     int i = 0;
//     string str;
//     while (getline(input, str)) {
//         lines[i] = str;
//         ++i;
//     }
//     input.close();

//     int ans = 0;
//     for (int i = 0; i < 1000; ++i) {
//         string cur = lines[i];
//         bool firstFound = false;
//         int found;
//         int cur_s;
//         for (int j = 0; j < cur.length(); ++j) {
//             if (isdigit(cur[j])) {
//                 if (!firstFound) firstFound = true, found = cur[j];
//                 cur_s = cur[j];
//             }
//         }
//         string fin;
//         fin += found;
//         fin += cur_s;
//         int num = stoi(fin);
//         ans += num;
//     }

//     cout << ans << '\n';

//     return 0;
// }
