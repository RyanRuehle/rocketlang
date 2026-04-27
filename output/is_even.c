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
    char number[256];
    char result[256];
    printf("%s\n", "Enter an integer:");
    scanf("%255s", number);
    if (is_even_without_modulo(atoi(number))) strcpy(result, "true");
    else strcpy(result, "false");
    printf("%s\n", result);
    return 0;
}