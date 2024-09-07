#include <iostream>
#include <fstream>
#include <string>
#include "style.hpp"

int main(){
    auto words = {"C", "**", "*C++*", "*Java", "*Python*", "Rust*"};

    std::ofstream out("out2.html");
    std::streambuf *coutbuf = std::cout.rdbuf();
    std::cout.rdbuf(out.rdbuf());

    std::cout << "<table>" << std::endl;
    std::cout << "<tr>" << std::endl;
    std::cout << "<th></th>" << std::endl;
    std::cout << "<th>Unstylized</th>" << std::endl;
    std::cout << "<th>Stylized</th>" << std::endl;
    std::cout << "</tr>" << std::endl;

    for (const auto& w: words) {
        std::cout << "<tr>" << std::endl;
        std::cout << "<td>" << w << "</td>" << std::endl;
        std::cout << "<td>" << sty::unstylize(w) << "</td>" << std::endl;
        std::cout << "<td>" << sty::stylize(w) << "</td>" << std::endl;
        std::cout << "</tr>" << std::endl;
    }

    std::cout << "</table>" << std::endl;

    return 0;
}