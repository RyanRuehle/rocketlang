#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int is_integer_string(char text[]) {
    int i = 0;
    if (text[0] == '\0') return 0;
    if (text[0] == '-' && text[1] != '\0') i = 1;
    for (; text[i] != '\0'; i++) {
        if (text[i] < '0' || text[i] > '9') return 0;
    }
    return 1;
}

int is_divisible(int number, int divisor) {
    if (divisor == 0) return 0;
    return number % divisor == 0;
}

int main() {
    char temp[256];
    char divisor[256];
    char number[256];
    char result[256];
    printf("%s\n", "Enter an integer:");
    scanf("%255s", number);
    strcpy(divisor, "2");
    if (!is_integer_string(number) || !is_integer_string(divisor)) {
        printf("%s\n", "Input was not a number.");
        strcpy(result, "false");
    }
    else if (atoi(divisor) == 0) {
        printf("%s\n", "Cannot divide by zero.");
        strcpy(result, "false");
    }
    else if (is_divisible(atoi(number), atoi(divisor))) strcpy(result, "true");
    else strcpy(result, "false");
    printf("%s\n", result);
    return 0;
}