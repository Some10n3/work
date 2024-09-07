#ifndef stylize_HPP
#define stylize_HPP
#include <string>
class sty{
    public:
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
                count++;
            }
            return output;
        }
        static auto stylize(const std::string& s){
            std::string output;
            int count = 0;
            for (const auto& c: s) {
                if (c == '*' && count == 0 && s.front() == '*' && s.back() == '*'){
                    output += "<strong>";
                }
                else if (c == '*' && count == s.size() - 1 && s.front() == '*' && s.back() == '*'){
                    output += "</strong>";
                }
                else if (s.front() == '*' && s.back() == '*' && count != 0 && count != s.size() - 1){
                    output += c;
                }
                else if ((s.front() == '*' && s.back() == '*') == false){
                    output += c;
                }
                count++;
            }
            return output;
        }
};
#endif