#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> array(n);
    for (int i = 0; i < n; ++i) {
        int t, b;
        cin >> t >> b;
        array[i] = {b, t};  // store as (b, l)
    }

    sort(array.begin(), array.end());
    pair<int, int> base = array[0];
    array.erase(array.begin());

    // Use a max-heap with priority_queue
    priority_queue<tuple<int, int, int>> heap;
    for (int i = 0; i < n - 1; ++i) {
        int b = array[i].first;
        int l = array[i].second;
        heap.emplace(-l, b, i);
    }

    unordered_map<pair<int, int>, int> hashMap;
    int total = base.second;

    for (int i = 0; i < k - 1 && !heap.empty(); ++i) {
        auto [l, b, _] = heap.top();
        heap.pop();
        total += -l;
        hashMap[{-l, b}]++;
    }

    long long ans = static_cast<long long>(base.first) * total;
    total -= base.second;

    for (int i = 0; i < n - 1; ++i) {
        int b = array[i].first;
        int l = array[i].second;
        if (hashMap[{-l, b}]) {
            hashMap[{-l, b}]--;
            if (hashMap[{-l, b}] == 0) {
                hashMap.erase({-l, b});
            }
        
            while (!heap.empty()) {
                auto [c, d, index] = heap.top();
                heap.pop();
                if (index < i) {
                    continue;
                }
                hashMap[{c, d}]++;
                total += -c;
                break;
            }
        } else {
            total += l;
        }

        ans = max(ans, static_cast<long long>(total) * b);
        total -= l;
    }

    cout << ans << endl;

    return 0;
}
