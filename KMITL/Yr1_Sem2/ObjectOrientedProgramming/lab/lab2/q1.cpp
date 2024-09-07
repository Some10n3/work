#include <iostream>
#include <string>
using namespace std;

string pattern1(int len){
    string output;
    for (int i = 0; i < len; i++){
        for (int j = -1; j < i; j++){
            output += "*";
        }
        output += "\n";
    }
    return output;
}
string pattern2(int len){
    string output;
    output += pattern1(len);
    for (int i = len - 1; i > 0; i--){
        for (int j = i; j > 0; j--){
            output += "*";
        }
        output += "\n";
    }
    return output;
}
string pattern3(int len){
    string output;
    for (int i = 0; i < len; i++){
        for (int j = 0; j < len - i - 1; j++){
            output += " ";
        }
        for (int j = 0; j < i + 1; j++){
            output += "*";
        }
        output += "\n";
    }
    for (int i = len - 1; i > 0; i--){
        for (int j = 0; j < len - i; j++){
            output += " ";
        }
        for (int j = 0; j < i; j++){
            output += "*";
        }
        output += "\n";
    }
    return output;
}

int main(){
    cout << "Please enter length: ";
    int len;
    cin >> len;
    auto output = pattern1(len);
    cout << output << endl;
    output = pattern2(len);
    cout << output << endl;
    output = pattern3(len);
    cout << output << endl;

    return 0;
}