#include <range/v3/all.hpp>

#include <iostream>

int main()
{
    auto v = {20, 10, 15};
    auto r_inv = v | ranges::views::transform([](int x){ return 1.0 / x; });

    // [0.05,0.1,0.0666667]
    auto val = 1.0 / ranges::accumulate(r_inv,0.0);
        // 1.0 / 0.216667 = 4.61538
    std::cout << val << std::endl;
}
