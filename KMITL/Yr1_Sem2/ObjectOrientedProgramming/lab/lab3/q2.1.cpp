#include <iostream>
#include <string>
#include <vector>

using std::vector;

vector<std::string> extract_attrs(vector<std::string>& words){
    vector<std::string> attrs;
    for (auto it = words.begin(); it != words.end();){
        if (it->find("[[") == 0 && it->find("]]") == it->size() - 2){
            attrs.push_back(*it);
            it = words.erase(it);
        } else {
            ++it;
        }
    }
    return attrs;
}

void print_words(const vector<std::string>& words, std::ostream& cout){
    for (const auto& word : words){
        std::cout << word << ", ";
    }
    std::cout << std::endl << std::endl;
}

int main(){
    const vector<std::string> test_words = {"switch", "[[noreturn]]", "if", "[[maybe_unused", "for", "[[fallthrough]]"};
    auto non_attrs = test_words;
    auto attrs = extract_attrs(non_attrs);
    std::cout << "Test words: ";
    print_words(test_words, std::cout);
    std::cout << "Attributes: ";
    print_words(attrs, std::cout);
    std::cout << "Non attributes: ";
    print_words(non_attrs, std::cout);
}