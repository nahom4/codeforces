#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, s;
        cin >> n >> s;
        
        vector<int> nums(n);
        vector<int> prefix(n + 1, 0);
        
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int mx = upper_bound(prefix.begin(), prefix.end() - 1, s) - prefix.begin();
        int index = 0;

        for (int i = 0; i < n; ++i) {
            int t = s - prefix[i];
            int target = prefix[i + 1] + t;
            int idx = upper_bound(prefix.begin(), prefix.end() - 1, target) - prefix.begin();
            
            if (t < 0) {
                break;
            }
            if (idx > mx) {
                index = i + 1;
                mx = max(mx, idx);
            }
        }
        
        if (index == 0) {
            cout << index << endl;
        } else {
            cout << index << endl;
        }
    }

    return 0;
}
