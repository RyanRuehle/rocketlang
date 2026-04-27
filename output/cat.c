#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_even_without_modulo(int number) {
    if (number < 0) number = -number;
    while (number > 1) {
        number = number - 2;
    }
    return number == 0;
}

int main() {
    char temp[256];
    char text[256];
    printf("%s\n", "Type something:");
    scanf("%255s", text);
    printf("%s\n", text);
    return 0;
}