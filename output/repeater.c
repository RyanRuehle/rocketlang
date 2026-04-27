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
    char char[256];
    char count[256];
    char result[256];
    printf("%s\n", "Enter a character:");
    scanf("%255s", char);
    printf("%s\n", "Enter how many times to repeat it:");
    scanf("%255s", count);
    result[0] = '\0';
    for (int i = 0; i < atoi(count); i++) {
        strcat(result, char);
    }
    printf("%s\n", result);
    return 0;
}