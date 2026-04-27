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
    char first[256];
    char result[256];
    char second[256];
    printf("%s\n", "Enter first single digit number:");
    scanf("%255s", first);
    printf("%s\n", "Enter second single digit number:");
    scanf("%255s", second);
    sprintf(result, "%d", atoi(first) * atoi(second));
    printf("%s\n", result);
    return 0;
}