#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using std::cout; using std::endl; using std::string; using std::cin;

inline bool space(char c) { return std::isspace(c); }
inline bool not_space(char c) { return !std::isspace(c); }

template <class Out> // changed
void split(const std::string& str, Out os){
    auto i = str.begin();
    while (i != str.end()) {
        i = find_if(i, str.end(), not_space);
        auto j = find_if(i, str.end(), space);
        if (i != str.end()){
            *os++ = string(i, j);
        }
        i = j;
    }
}

static auto unstylize(const std::string& s){
    std::string output;
    int count = 0;
    for (const auto& c: s) {
        if (s.front() == '*' && s.back() == '*' && count != 0 && count != s.size() - 1){
            output += c;
        }
        else if ((s.front() == '*' && s.back() == '*') == false){
            output += c;
        }
        else if (s.size() == 1){
            output += c;
        }
        count++;
    }
    return output;
}

auto unstylizedWord(std::vector<string> words){
    std::vector<string> unstylizedWords;
    cout << "Unstylized: ";
    for (auto i : words) {
        cout << unstylize(i) << " ";
        unstylizedWords.push_back(unstylize(i));
    }
    cout << endl;
    return unstylizedWords;
}

void reverse(std::vector<string> words){
    cout << "Reverse: ";
    for (int i = words.size() - 1; i >= 0; i--) {
        cout << words[i] << " ";
    }
    cout << endl;
}

void alphabetical(std::vector<string> words){
    cout << "Alphabetical: ";
    sort(words.begin(), words.end());
    for (auto i : words) {
        cout << i << " ";
    }
    cout << endl;
}

int main(){
    string input;
    std::vector<string> words;
    std::vector<string> unstylizedWords;
    cout << "Enter a string: ";
    getline(cin, input);
    split(input, back_inserter(words));
    unstylizedWords = unstylizedWord(words);
    reverse(unstylizedWords);
    alphabetical(unstylizedWords);
    cout << endl;
        
    return 0;
}

//C *C++* Rust* *Python* * *Java