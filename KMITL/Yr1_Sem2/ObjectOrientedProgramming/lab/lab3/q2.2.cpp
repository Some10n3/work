#include <iostream>
#include <string>
#include <vector>

using std::string;
using std::vector;

void extract_attrs(const vector<string>& words, vector<string>& attrs, vector<string>& non_attrs){
    for (const auto& word : words){
        if (word.find("[[") == 0 && word.find("]]") == word.size() - 2){
            attrs.push_back(word);
        } else {
            non_attrs.push_back(word);
        }
    }
}

std::ostream& print_words(std::ostream& cout, const vector<string>& words){
    for (const auto& word : words){
        cout << word << "\", \"";
    }
    return cout;
}

int main(){
    const vector<std::string> test_words = {"switch", "[[noreturn]]", "if", "[[maybe_unused", "for", "[[fallthrough]]"};
    vector<string> attrs, non_attrs;
    extract_attrs(test_words, attrs, non_attrs);
    std::cout << "Test words: {\"";
    print_words(std::cout, test_words);
    std::cout << "}" <<std::endl << "Attributes: {\"";
    print_words(std::cout, attrs);
    std::cout << "}" <<std::endl << "Non attributes: {\"";
    print_words(std::cout, non_attrs);
    std::cout << "}" <<std::endl;
}