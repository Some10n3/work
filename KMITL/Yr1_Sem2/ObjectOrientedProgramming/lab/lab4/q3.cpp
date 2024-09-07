#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>
#include <map>

using std::cout; using std::cin; using std::endl; using std::sort; using std::vector; using std::list; using std::copy; using std::string; using std::back_inserter; using std::find_if;

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


std::map<std::string, int> mapp(std::map<std::string, int> map, vector<string> v){
    int count = 1;
    string temp;
    for (auto i : v) {
        if (count % 2 == 0) {
            if (map.find(temp) != map.end()) {
                map[temp] += std::stoi(i);
            }
            else {
                map.insert(std::pair<string, int>(temp, std::stoi(i)));
            }
        }
        else {
            temp = i;
        }
        count++;
    }
    return map;
}

std::map<std::string, string> mappp(std::map<std::string, string> map, vector<string> v){
    int count = 1;
    string temp;
    for (string i : v) {
        if (count % 2 == 0) {
            if (map.find(temp) != map.end()) {
                map[temp] = map[temp] + ", " + i;
            }
            else {
                map.insert(std::pair<string, string>(temp, i));
            }
        }
        else {
            temp = i;
        }
        count++;
    }
    return map;
}

int main(){
    std::map<std::string, int> map;
    std::map<std::string, string> map2;
    string x;
    cout << "Enter a string: ";
    std::getline(cin, x);
    vector<string> v;
    cout << "Results : " << endl;
    split(x, back_inserter(v));
    map = mapp(map, v);
    for (auto i : map) {
        cout << i.first << " : " << i.second << endl;
    }
    cout << endl << "Results : " << endl;
    map2 = mappp(map2, v);
    for (auto i : map2) {
        cout << i.first << " : " << i.second << endl;
    }
    return 0;
}//a 3 b 2 a 1 c 7 b 5 c 2 b 3