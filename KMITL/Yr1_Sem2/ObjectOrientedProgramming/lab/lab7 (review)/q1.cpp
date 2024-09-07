#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using std::cin; using std::cout; using std::endl; using std::string; using std::vector; using std::pair;

int cStyleSize(const char* arr){
    int i = 0;
    while(arr[i] != '\0'){
        i++;
    }
    return i;
}

string substitute(string& text, string word, string rep){
    string result;
    for(int i = 0; i < text.size(); i++){
        if(text[i] == word[0]){
            bool match = true;
            for(int j = 0; j < word.size(); j++){
                if(text[i + j] != word[j]){
                    match = false;
                    break;
                }
            }
            if(match){
                result += rep;
                i += word.size() - 1;
            } else {
                result += text[i];
            }
        } else {
            result += text[i];
        }
    }
    return result;
}

char* substitute2(char* text, char* word, char* rep){
    char* result;
    int i = 0;
    int j = 0;
    while(*(text + i) != '\0'){
        if(*(text + i) == word[0]){
            bool match = true;
            for(int j = 0; j < cStyleSize(word); j++){
                if(*(text + i + j) != *(word + j)){
                    match = false;
                    break;
                }
            }
            if(match){
                for(int k = 0; k < cStyleSize(rep); k++){
                    *(result + j) = *(rep + k);
                    j++;
                }
                i += cStyleSize(word) - 1;
            } else {
                *(result + j) = *(text + i);
                j++;
            }
        } else {
            *(result + j) = *(text + i);
            j++;
        }
        i++;
    }
    return result;
}

vector<pair<double, double>> createPairs(const vector<double>& arr){
    vector<pair<double, double>> result;
    for(int i = 0; i < arr.size(); i++){
        if (i + 1 < arr.size()){
            result.push_back({arr[i], arr[i + 1]});
        }
        i++;
    }
    return result;
}

vector<pair<string, string>> createPairs2(const char*& arr){
    vector<pair<string, string>> result;
    for (int i = 0; i < cStyleSize(arr); i++){
        if (i + 1 < cStyleSize(arr)){
            result.push_back({string(1, arr[i]), string(1, arr[i + 1])});
        }
        i++;
    }
    return result;
}

vector<pair<char*,char*>> create_pairs_cstyle(const char* arr){
    vector<pair<char*, char*>> pairs;
    int i = 0;
    while (arr[i] != '\0') {
        int j = i;
        while (arr[j] != ' ' && arr[j] != '\0') {
            j++;
        }
        int len1 = j - i;
        char* str1 = new char[len1 + 1];
        for (int k = 0; k < len1; k++) {
            str1[k] = arr[i + k];
        }
        str1[len1] = '\0';
        i = j + 1;
        j = i;
        while (arr[j] != ' ' && arr[j] != '\0') {
            j++;
        }
        int len2 = j - i;
        char* str2 = new char[len2 + 1];
        for (int k = 0; k < len2; k++) {
            str2[k] = arr[i + k];
        }
        str2[len2] = '\0';
        i = j + 1;
        if (len1 == 0 || len2 == 0) break;
        pairs.push_back({str1, str2});
    }
    return pairs;
}


int main(){
    string text1 = "abc python javapythonx";
    string text2 = "abcx yja helx yz01 23";

    cout << substitute(text1, "python", "rust") << endl;
    cout << substitute(text1, "", "rust") << endl;
    cout << substitute(text2, "python", "rust") << endl;
    cout << substitute(text2, "x y", "a b") << endl;

    cout << endl << endl;

    cout << substitute(text1, "python", "rust") << endl;
    cout << substitute(text1, "", "rust") << endl;
    cout << substitute(text2, "python", "rust") << endl;
    cout << substitute(text2, "x y", "a b") << endl;
/*
    char text3[] = "abc python javapythonx";
    char text4[] = "abcx yja helx yz01 23";

    char a[] = "python";
    char b[] = "rust";
    char c[] = "";
    char d[] = "x y";
    char e[] = "a b";

    cout << substitute2(text3, a, b) << endl;
    cout << substitute2(text3, c, b) << endl;
    cout << substitute2(text4, a, b) << endl;
    cout << substitute2(text4, d, e) << endl;
*/
    vector<double> arr = {1, 2, 3, 4, 5, 6, 7};
    vector<pair<double, double>> pairs = createPairs(arr);
    for(auto p : pairs){
        cout << "(" << p.first << ", " << p.second << ") ";
    }

    cout << endl << endl;

    char arr2[] = "0 9 8 7 6 5 4 3";
    vector<pair<char*, char*>> pairs2 = create_pairs_cstyle(arr2);

    for(auto p : pairs2){
        cout << "(" << p.first << ", " << p.second << ") ";
    }


    return 0;
}