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

string splitString(const string& str, string& words, string& words2){
    istringstream iss(str);
    string word;
    getline(iss, words, ';');
    getline(iss, word, ';');
    getline(iss, words2);
    return word;
}

vector<float> vecStrToFloat(vector<string> words){
    vector<float> v;
    for (auto i : words) {
        v.push_back(stof(i));
    }
    return v;
}

float avgInVec(vector<float> v){
    float sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v[i];
    }
    return sum / v.size();
}

string cartesianProduct(vector<string> words, vector<string> words2, vector<string> words3){
    string output;
    for (int i = 0; i < words.size(); i++) {
        for (int j = 0; j < words2.size(); j++) {
            for (int k = 0; k < words3.size(); k++) {
                output += "(" + words[i] + ", " + words2[j] + ", " + words3[k] + "), ";
            }
        }
    }
    return output;
}

int main(){
    const string fileName = "data3.txt";
    string s;
    string word;
    string word2;
    string word3;
    ifstream file(fileName);
    const string delim = " ";

    cout << "<" << fileName << ">\n\n";

    getline(file, s);
    word2 = splitString(s, word, word3);

    vector<string> words;
    words = split(word, delim);
    vector<string> words2;
    words2 = split(word2, delim);
    vector<string> words3;
    words3 = split(word3, delim);

    vector<float> v1;
    v1 = vecStrToFloat(words);
    vector<float> v2;
    v2 = vecStrToFloat(words2);
    vector<float> v3;
    v3 = vecStrToFloat(words3);
    
    cout << "vec1 :\n";
    for (auto i : words) {
        cout << i << endl;
    }
    cout << "vec2 :\n";
    for (auto i : words2) {
        cout << i << endl;
    }
    cout << "vec3 :\n";
    for (auto i : words3) {
        cout << i << endl;
    }
    
    cout << "Average of v1: " << avgInVec(v1) << endl;
    cout << "Average of v2: " << avgInVec(v2) << endl;
    cout << "Average of v3: " << avgInVec(v3) << endl;
    cout << "\n\n";

    cout << "Cartesian Product of v1, v2, v3:\n";
    cout << cartesianProduct(words, words2, words3) << endl;


    return 0;
}