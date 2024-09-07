#include <iostream>

void inverse_numbers(double* v, size_t n){
    for (int i = 0; i < n; i++) {
        v[i] = -1 * v[i];
    }
}

void replace(char* s, char c1, char c2) {
    while (*s) {
        if (*s == c1) {
            *s = c2;
        }
        s++;
    }
}
int strlen(const char* s) {
    int i = 0;
    while (*s) {
        i++;
        s++;
    }
    return i;
}

char* encode_hex(const char* s) {
    const char hex[] = "0123456789ABCDEF";
    const int length = strlen(s);
    char* encoded = new char[length * 2 + 1];

    for (int i = 0; i < length; i++) {
        encoded[i * 2] = hex[(s[i] >> 4) & 0xF];
        encoded[i * 2 + 1] = hex[s[i] & 0xF];
    }

    encoded[length * 2] = '\0';
    return encoded;
}

int main (){
    double v[] = {1, 2, 3, 4, 5};
    inverse_numbers(v, 2);
    std::cout << "when n = 2" << std::endl;
    for (int i = 0; i < 5; i++) {
        std::cout << v[i] << std::endl;
    }
    std::cout << std::endl;

    inverse_numbers(v, 5);
    std::cout << "when n = 5" << std::endl;
    for (int i = 0; i < 5; i++) {
        std::cout << v[i] << std::endl;
    }
    std::cout << std::endl;

    char s[] = "hello world";
    std::cout << "Replacing l with X in -->" << s << std::endl;
    replace(s, 'l', 'X');
    std::cout << s << std::endl;
    std::cout << std::endl;

    std::cout << "Encoding hello world to hex" << std::endl;
    char* hex = encode_hex("hello world");
    std::cout << hex << std::endl;
    delete[] hex;
    std::cout << std::endl;

    return 0;
}