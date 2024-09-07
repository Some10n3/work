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

string splitString(const string& str, string& words){
    istringstream iss(str);
    string word;
    getline(iss, words, ';');
    getline(iss, word);
    return word;
}

string interleave(vector<string> words, vector<string> words2){
    string output;
    if (words.size() > words2.size()){
        for (int i = 0; i < words2.size(); i++) {
            output += words[i] + " " + words2[i] + " ";
        }
        for (int i = words2.size(); i < words.size(); i++) {
            output += words[i] + " ";
        }
    }
    else {
        for (int i = 0; i < words.size(); i++) {
            output += words[i] + " " + words2[i] + " ";
        }
        for (int i = words.size(); i < words2.size(); i++) {
            output += words2[i] + " ";
        }
    }
    return output;
}

float sumOfProducts(vector<float> v1, vector<float> v2){
    float sum = 0;
    if (v1.size() > v2.size()){
        for (int i = 0; i < v2.size(); i++) {
            sum += v1[i] * v2[i];
        }
    }
    else{
        for (int i = 0; i < v1.size(); i++) {
            sum += v1[i] * v2[i];
        }
    }
    return sum;
}

vector<float> vecStrToFloat(vector<string> words){
    vector<float> v;
    for (auto i : words) {
        v.push_back(stof(i));
    }
    return v;
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

int main () {
    const string fileName = "data2.txt";
    string s;
    string word;
    string word2;
    ifstream file(fileName);
    const string delim = " ";

    cout << "<" << fileName << ">\n\n";

    getline(file, s);
    word2 = splitString(s, word);

    vector<string> words;
    words = split(word, delim);
    vector<string> words2;
    words2 = split(word2, delim);
    
    cout << "Interleave : \n";
    cout << interleave(words, words2) << "\n\n";

    cout << "Sum of products : \n";
    vector<float> v1 = vecStrToFloat(words);
    vector<float> v2 = vecStrToFloat(words2);
    cout << sumOfProducts(v1, v2) << "\n\n";

    cout << "Cartesian product : \n";
    vector<string> v = cartesianProd(words, words2);
    for (auto i : v) {
        cout << i << " ";
    }
    cout << "\n\n";

    return 0;
}