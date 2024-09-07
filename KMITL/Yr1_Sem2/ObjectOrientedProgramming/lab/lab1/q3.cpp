#include <iostream>
#include <string>
using namespace std;

void star_1(int len){
    for (int i = 0; i < len; i++){
        for (int j = -1; j < i; j++){
            cout << "*";
        }
        cout << endl;
    }
}
void star_2(int len){
    star_1(len);
    for (int i = len - 1; i > 0; i--){
        for (int j = i; j > 0; j--){
            cout << "*";
        }
        cout << endl;
    }
}
void star_3(int len){
    for (int i = 0; i < len; i++){
        for (int j = 0; j < len - i - 1; j++){
            cout << " ";
        }
        for (int j = 0; j < i + 1; j++){
            cout << "*";
        }
        cout << endl;
    }
    for (int i = len - 1; i > 0; i--){
        for (int j = 0; j < len - i; j++){
            cout << " ";
        }
        for (int j = 0; j < i; j++){
            cout << "*";
        }
        cout << endl;
    }
}
int main(){
    cout << "Please enter length: ";
    int len;
    cin >> len;
    star_1(len);
    cout << endl;
    star_2(len);
    cout << endl;
    star_3(len);

    return 0;
}