#include <iostream>

class BaseClass {
   public:
    int a;
    void func() {
        std::cout << "Function of BaseClass" << std::endl;
    }
};

class DerivedClass : public BaseClass {
   public:
    int b;
    void derivedFunc() {
        std::cout << "Function of DerivedClass" << std::endl;
    }
};

int main() {
    DerivedClass obj;
    obj.a = 10;
    obj.b = 20;
    obj.func();         // Output: Function of BaseClass
    obj.derivedFunc();  // Output: Function of DerivedClass
    std::cout << obj.a << std::endl;  // Output: 10
    std::cout << obj.b << std::endl;  // Output: 20
    return 0;
}