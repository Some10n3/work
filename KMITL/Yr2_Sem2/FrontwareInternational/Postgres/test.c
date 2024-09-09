#include <stdio.h>

int main() {
    printf("Hello, World!\n");

    int a = 10;
    int b = 20;
    int c = a + b;

    printf("a + b = %d\n", c);

    for (int i = 0; i < 10; i++) {
        printf("i = %d\n", i);
    }

    while (a < 20) {
        printf("a = %d\n", a);
        a++;
    }

    

    return 0;
}