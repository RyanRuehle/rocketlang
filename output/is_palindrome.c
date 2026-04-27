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
    char result[256];
    char word[256];
    printf("%s\n", "Enter a word:");
    scanf("%255s", word);
    strcpy(temp, word);
    int len_result = strlen(temp);
    int same_result = 1;
    for (int i = 0; i < len_result; i++) {
        if (temp[i] != temp[len_result - i - 1]) same_result = 0;
    }
    if (same_result) strcpy(result, "true");
    else strcpy(result, "false");
    printf("%s\n", result);
    return 0;
}