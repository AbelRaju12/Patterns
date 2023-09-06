// t
// to
// tom
// toma
// tomat
// tomato
// tomato
// omato
// mato
// ato
// to
// o

#include <stdio.h>
#include <stdlib.h>
int main(){
    char str[20];
    int count = 0;
    printf("Enter a string: ");
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++){
        for(int j = 0; j <= i; j++){
            printf("%c", str[j]);
        }
        printf("\n");
    }
    for(int i = 0; i < count; i++){
        for(int j = i; j < count; j++){
            printf("%c", str[j]);
        }
        printf("\n");
    }
    return 0;
}