#include <iostream>
#include <string>
using namespace std;
void star2_2(string p1_name, string p2_name){
    int len1 = p1_name.length();
    int len2 = p2_name.length();
    for (int i = 0; i < 27 + len1 + len2; i++){
        cout << "*";
    }
    cout << endl << "*";
    for (int i = 0; i < 12 + len1; i++){
        cout << " ";
    }
    cout << "*";
    for (int i = 0; i < 12 + len2; i++){
        cout << " ";
    }
    cout << "*" << endl;
    cout << "* Player 1: " << p1_name << " * Player 2: " << p2_name << " *" << endl;
    cout << "*";
    for (int i = 0; i < 12 + len1; i++){
        cout << " ";
    }
    cout << "*";
    for (int i = 0; i < 12 + len2; i++){
        cout << " ";
    }
    cout << "*" << endl;
    for (int i = 0; i < 27 + len1 + len2; i++){
        cout << "*";
    }
}
void star2_3_a(string p1_name, string p2_name){
    int len1 = p1_name.length();
    int len2 = p2_name.length();
    int len;
    if (len1 >= len2){
        len = len1;
    }
    else{
        len = len2;
    }

    for (int i = 0; i < 14 + len; i++){
        cout << "*";
    }
    cout << endl << "*";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "*" << endl;
    if (len > len1){
        cout << "* Player 1: " << p1_name;
        for (int i = 0; i < len - len1 + 1; i++){
            cout << " ";
        }
        cout << "*";
    }
    else{
        cout << "* Player 1: " << p1_name << " *";
    }
    cout << endl << "*";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "*" << endl;
    for (int i = 0; i < 14 + len; i++){
        cout << "*";
    }
    cout << endl << "*";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "*" << endl;
    if (len > len2){
        cout << "* Player 2: " << p2_name;
        for (int i = 0; i < len - len2 + 1; i++){
            cout << " ";
        }
        cout << "*";
    }
    else{
        cout << "* Player 2: " << p2_name << " *";
    }
    cout << endl << "*";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "*" << endl;
    for (int i = 0; i < 14 + len; i++){
        cout << "*";
    }

}
void star2_3_b(string p1_name, string p2_name){
    int len1 = p1_name.length();
    int len2 = p2_name.length();
    int len;
    if (len1 >= len2){
        len = len1;
    }
    else{
        len = len2;
    }
    cout << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "-";
    }
    cout << "+" << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl;
    if (len > len1){
        cout << "| Player 1: " << p1_name;
        for (int i = 0; i < len - len1 + 1; i++){
            cout << " ";
        }
        cout << "|";
    }
    else{
        cout << "| Player 1: " << p1_name << " |";
    }
    cout << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "-";
    }
    cout << "+" << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl;
    if (len > len2){
        cout << "| Player 2: " << p2_name;
        for (int i = 0; i < len - len2 + 1; i++){
            cout << " ";
        }
        cout << "|";
    }
    else{
        cout << "| Player 2: " << p2_name << " |";
    }
    cout << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "-";
    }
    cout << "+";
}
void star2_3_c(string p1_name, string p2_name){
    int len1 = p1_name.length();
    int len2 = p2_name.length();
    int len;
    if (len1 >= len2){
        len = len1;
    }
    else{
        len = len2;
    }
    cout << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "=";
    }
    cout << "+" << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl;
    if (len > len1){
        cout << "| Player 1: " << p1_name;
        for (int i = 0; i < len - len1 + 1; i++){
            cout << " ";
        }
        cout << "|";
    }
    else{
        cout << "| Player 1: " << p1_name << " |";
    }
    cout << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "-";
    }
    cout << "+" << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl;
    if (len > len2){
        cout << "| Player 2: " << p2_name;
        for (int i = 0; i < len - len2 + 1; i++){
            cout << " ";
        }
        cout << "|";
    }
    else{
        cout << "| Player 2: " << p2_name << " |";
    }
    cout << endl << "|";
    for (int i = 0; i < 12 + len; i++){
        cout << " ";
    }
    cout << "|" << endl << "+";
    for (int i = 0; i < 12 + len; i++){
        cout << "=";
    }
    cout << "+";
}
int main(){
    cout << "Please enter P1 name: ";
    string p1_name;
    cin >> p1_name;
    cout << "Please enter P2 name: ";
    string p2_name;
    cin >> p2_name;
    star2_2(p1_name, p2_name);
    cout << endl;
    star2_3_a(p1_name, p2_name);
    cout << endl;
    star2_3_b(p1_name, p2_name);
    cout << endl;
    star2_3_c(p1_name, p2_name);
    return 0;
}