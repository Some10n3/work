#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using std::cout;
using std::cin; 
using std::endl;
using std::sort;
using std::vector; 
using std::copy;
using std::string;

bool is_prime(int n){
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0){
        if (n == 2 || n == 3 || n == 5) return true;
        return false;
    }
        // check through all numbers of the form i = 6k - 1 and i = 6k + 1
    for (int i = 5; i * i < n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0){
            return false; // n is divisible by i or i + 2
        }
        return true; // no divisor within [5, n) found
    }
}

template <class T>
T median(std::vector<T> vec){
    sort(vec.begin(), vec.end());
    using vec_sz = typename vector<T>::size_type;
    vec_sz size = vec.size();
    if (size == 0) throw std::domain_error("median of an empty vector");
    const auto mid = size / 2;

    return size % 2 != 0? vec[mid] : (vec[mid - 1] + vec[mid]) / 2;
}

int main(){
    cout << "Enter the upper limit: ";
    int n;
    cin >> n;
    for (int i = 2; i <= n; i += 1) {
        if (is_prime(i)){
            cout << i << endl;
        }
    }
    cout << endl;
    std::vector<float> vec_sample {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    cout << median<float>(vec_sample) << endl;
    return 0;
    
}