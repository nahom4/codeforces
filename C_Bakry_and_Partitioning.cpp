#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <functional>

using namespace std;

void solve() {
    int t;
    cin >> t;

    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> array(n);
        for (int i = 0; i < n; ++i) {
            cin >> array[i];
        }

        unordered_map<int, vector<int>> graph;
        for (int i = 0; i < n - 1; ++i) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int target = 0;
        for (int i = 0; i < n; ++i) {
            target ^= array[i];
        }

        unordered_set<int> visited;
        int cuts = 0;

        function<int(int)> dfs = [&](int node) {
            if (visited.count(node)) return 0;
            visited.insert(node);

            int curr = array[node - 1];
            for (int neighbor : graph[node]) {
                curr ^= dfs(neighbor);
            }

            if (curr == target) {
                cuts++;
                return 0;
            }
            cout<<cuts<<endl;
            return curr; 
        };

        cout<<cuts<< endl;
        if (target == 0 || (dfs(1) == 0 && cuts > 1 && cuts < k )) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}