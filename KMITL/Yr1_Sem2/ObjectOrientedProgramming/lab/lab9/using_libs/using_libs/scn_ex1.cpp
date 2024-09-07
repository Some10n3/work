#include <scn/scn.h>
#include <fmt/core.h>

int main()
{
    int i;
    // Read an integer from stdin with an accompanying message
    auto result = scn::prompt("What's your favorite number? ", "{}", i);
    if (result)
        fmt::print("Oh, cool, {}!\n", i);
    else
        fmt::print("{}\n", result.error().msg());

    double x, y;
    auto res2 = scn::scan(
        "    5:    [123,    3.14]   ",
        "{}: [{}, {}]", i, x, y);
    if (res2)
        fmt::print("{}: [{}, {}]\n", i, x, y);
    else
        fmt::print("{}\n", result.error().msg());
}
