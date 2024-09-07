#include <iostream>
using namespace std;

class room;
class dog;
class cat;

class room {
private:
protected:
public:
    dog* dog;
    cat* cat;

int gay(room& a, dog& b) {
    return 0;
}
    friend ;
};


class dog {
public:
    bool checkCat(room& r){
        if (r.cat == NULL) {
            return false;
        }
        else {
            return true;
        }
    }
};


int main() {
    cout << "Hello World!" << endl;
    int a;
    cout << "Enter a number: ";
    cin >> a;
    cout << a << endl;
    return 0;
}