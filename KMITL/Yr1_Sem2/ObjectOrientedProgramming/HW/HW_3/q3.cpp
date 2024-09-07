#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>

using std::cout; using std::endl; using std::string; using std::cin; using std::vector; using std::istringstream; using std::getline; using std::ifstream;

vector<string> split(const string& sOri, const string& delim) {
    vector<string> result;
    size_t start = 0;
    string c = sOri.substr(0, 1);
    string s;
    if (c == delim){
        s = sOri.substr(1);
    }
    else {
        s = sOri;
    }
    size_t end = s.find(delim);
    while (end != string::npos) {
        result.push_back(s.substr(start, end - start));
        start = end + delim.length();
        end = s.find(delim, start);
    }
    result.push_back(s.substr(start, end));
    return result;
}

bool styleCheck(const std::string& s){
    std::string output;
    if (s.front() == '*' && s.back() == '*'){
        return true;
    }
    else {
        return false;
    }
}

vector <string> cartesianProd(vector<string> words, vector<string> words2){
    vector<string> v;
    for (auto i : words) {
        for (auto j : words2) {
            v.push_back("(" + i + ", " + j + "), ");
        }
    }
    return v;
}

int main(){
    const string fileName = "data4.txt";
    string s;
    ifstream file(fileName);
    const string delim = " ";

    cout << "<" << fileName << ">\n\n";

    getline(file, s);
    vector<string> input = split(s, delim);
    vector<string> withStyle;
    vector<string> withoutStyle;
    for (const auto& i: input) {
        if (styleCheck(i)){
            withStyle.push_back(i);
        }
        else {
            withoutStyle.push_back(i);
        }
    }
    cout << "With style: ";
    for (const auto& i: withStyle) {
        cout << i << " ";
    }
    cout << endl;
    cout << "Without style: ";
    for (const auto& i: withoutStyle) {
        cout << i << " ";
    }
    cout << endl;

    cout << "Cartesian product: ";
    vector<string> cartesian = cartesianProd(withStyle, withoutStyle);
    for (const auto& i: cartesian) {
        cout << i;
    }
    cout << endl;

    return 0;
}