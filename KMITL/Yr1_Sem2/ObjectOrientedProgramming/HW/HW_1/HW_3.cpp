#include <iostream>
#include <string>
#include <random>

using std::cout, std::cin, std::endl, std::string;

int main() {
    std::mt19937 rng;
    rng.seed(std::random_device()());
    std::uniform_real_distribution<double> dist{0, 1};
    
    int N;
    int i = 0;
    double sum = 0;

    cout << "Enter the N value: ";
    cin >> N;

    while(i < N){
        double x = dist(rng);
        
        double err = x - 0.5;
        sum += (err * err);
        i++;
    }

    double mean_squared_err = sum / N;

    cout << "Mean Squared Error: " << mean_squared_err << endl;
}