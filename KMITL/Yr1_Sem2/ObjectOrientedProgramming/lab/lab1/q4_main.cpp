//// lab1_3.cpp
#include "q4_random.hpp"
#include <iomanip>
#include <iostream>
#include <vector>

template<typename T_>
inline constexpr
T_ pi_v{3.141592653589793238462643383279502884L};
inline constexpr double pi = pi_v<double>;
int main()
{
constexpr double rnd_min = -1.0, rnd_max = 1.0;
Rand_double rnd{rnd_min, rnd_max};
std::random_device rd;
rnd.seed(rd());
std::cout << std::fixed << std::setprecision(3);

double x;
double y;

int N = 100;
int Ni = 0;
for (int i = 0; i < N; i++){
    x = rnd();
    y = rnd();
    if ((std::sqrt(x*x + y*y) <= 1.0) && (std::sqrt(x*x + y*y) >= -1.0)){
        Ni++;
    }
}

double Pi = 4.0 * Ni / N;
std::cout << "Pi = " << Pi << std::endl;
double error = std::abs(Pi - pi);
std::cout << "Relative Error = " << error << std::endl;
double percent = error / pi * 100;
std::cout << "Percent Error = " << percent << "%" << std::endl;
return 0;
}