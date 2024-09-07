#include <string>
class City {
public:
const std::string& name() const
{ return n; }
double temperature() const
{ return temp; }
City(): n{}, temp{} {}
explicit City(double t)
: n("Unknown"), temp{t} {}
private:
std::string n;
double temp;
};

double test1(City c)
{ return c.temperature(); }
double test2(const City& c)
{ return c.temperature(); }
City test3() { return City(34.5); }
#include <iostream>
int main()
{
City c;
std::cout << test1(c) << std::endl;
std::cout << test2(c) << std::endl;
std::cout << test3().temperature()
<< std::endl << std::endl;
std::cout << test1(City(15.2))
<< std::endl;
std::cout << test2(City(25.4))
<< std::endl;
  return 0;
}