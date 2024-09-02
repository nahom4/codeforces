#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

vector<int> SieveOfEratosthenes(int n) {
    // Initialize a vector to mark non-primes
    vector<bool> prime(n + 1, true);
    int p = 2;

    // Only iterate while p * p <= n (which is the square root of n)
    while (p * p <= n) {
        // If prime[p] is still True, then it's a prime
        if (prime[p]) {
            // Mark multiples of p as non-prime
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
        p++;
    }

    // Collect primes up to sqrt(n)
    vector<int> target;
    for (int p = 2; p <= n; p++) {
        if (prime[p]) {
            target.push_back(p);
        }
    }

    return target;
}

int main() {
    int n;
    cin >> n;
    vector<int> array(n);
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }

    int maxElement = *max_element(array.begin(), array.end());
    int sqrtMax = ceil(sqrt(maxElement));
    vector<int> target = SieveOfEratosthenes(sqrtMax);

    vector<int> first(n, -1);
    vector<int> second(n, -1);

    for (int i = 0; i < n; i++) {
        int num = array[i];
        for (int prime : target) {
            if (num % prime == 0) {
                while (num > 1 && num % prime == 0) {
                    num /= prime;
                }
                if (num > 1) {
                    first[i] = prime;
                    second[i] = num;
                }
                break;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << first[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << second[i] << " ";
    }
    cout << endl;

    return 0;
}
