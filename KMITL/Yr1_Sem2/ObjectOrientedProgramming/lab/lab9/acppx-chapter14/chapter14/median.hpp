#ifndef ACPP_MEDIAN_HPP
#define ACPP_MEDIAN_HPP

#include <algorithm>
#include <stdexcept>
#include <vector>

// `median.hpp' -- generic version
template <class T>
T median(std::vector<T> vec)
{
    using std::domain_error;
    using std::sort;
    using std::vector;

    const auto size = vec.size();
    if (size == 0)
        throw domain_error("median of an empty vector");

    sort(vec.begin(), vec.end());

    const auto mid = size / 2;
    return size % 2 == 0? (vec[mid] + vec[mid - 1]) / 2: vec[mid];
}

#endif /* ACPP_MEDIAN_HPP */
