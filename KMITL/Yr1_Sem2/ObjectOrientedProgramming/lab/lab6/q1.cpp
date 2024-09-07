#include <iostream>
#include <vector>
#include <array>
#include <string>

void slashN() {
    std::cout << std::endl;
}

void to_upper(char* s){
    int i = 0;
    while (s[i] != '\0') {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = s[i] - 32;
        }
        i++;
    }
}

char* rev_dup (const char* s){
    //reverse 
    int i = 0;
    while (s[i] != '\0') {
        i++;
    }
    char* rev = new char[i + 1];
    int j = 0;
    while (i >= 0) {
        rev[j] = s[i];
        i--;
        j++;
    }
    rev[j] = '\0';
    for (int i = 0; i < j; i++) {
        std::cout << rev[i];
    }
    return rev;
}

char* read_text(std::istream& is){
    //read til exclaimation mark
    char c;
    int i = 0;
    char* s = new char[100];
    while (is.get(c)) {
        if (c == '!') {
            break;
        }
        s[i] = c;
        i++;
    }
    s[i] = '\0';



    return s;
}

int main()
{
    double coords[3] = {2, 3, 4};
    double* p1 = coords;
    
    std::array<double, 4> pt4d;
    auto arr_it = pt4d.begin();
    std::vector<double> vec;
    auto vec_it = vec.begin();

    std::cout << "Number of elements in coords : " << sizeof(coords) / sizeof(double) << std::endl;
    std::cout << "Size of coords : " << sizeof(coords) << std::endl;
    std::cout << "Size of p1 : " << sizeof(p1) << std::endl;
    std::cout << "Size of pt4d : " << sizeof(pt4d) << std::endl;
    std::cout << "Size of vec <";
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << ", ";
    }
    std::cout << "> : " << sizeof(vec) << std::endl;
    vec.push_back(1);
    std::cout << "Size of vec after push back <";
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << ", ";
    }
    std::cout << "> : " << sizeof(vec) << std::endl;
    vec.push_back(3);
    std::cout << "Size of vec after push back <";
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << ", ";
    }
    std::cout << "> : " << sizeof(vec) << std::endl;
    std::cout << "Why the hell they out put same size?";

    std::cout << "Size of arr_it : " << sizeof(arr_it) << std::endl;
    std::cout << "Size of vec_it : " << sizeof(vec_it) << std::endl;
    
    char a[] = "Hello, World!!!";
    to_upper(a);
    std::cout << a << std::endl;

    rev_dup(a);

    slashN();

    std::cout << "Enter a string: ";
    char* b = read_text(std::cin);
    std::cout << b << std::endl;
}