#include <iostream>
#include <string>
#include <iomanip>

using std::cout, std::cin, std::endl, std::string;

double F2C(double fh){
    return (fh - 32) * 5 / 9;
}

int main(){
    int fh = 300;
    cout << std::fixed << std::setprecision(1) << "Farenheir\tCelcius" << endl;
    while(fh >= 0){
        cout << fh << "\t" << F2C(fh) << endl;
        fh -= 20;
    }
    return 0;
}