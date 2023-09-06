// t
// to
// tom
// toma
// tomat
// tomato
// tomat
// toma
// tom
// to
// t

#include <stdio.h>
#include <stdlib.h>
void main(){
    char str[20];
    int  count = 0, k;
    printf("Enter a string: ");
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < (2 * count + 1); i++){
        if(i < count){
            k = i;
        }
        else{
            k = abs(2 * count - i);
        }
        for(int j = 0; j < k; j++){
            printf("%c", str[j]);
        }
        printf("\n");
    } 
    // for(int i = 0; i < count; i++){
    //     for(int j = 0; j <= i; j++){
    //         printf("%c", str[j]);
    //     }
    //     printf("\n");
    // }  
    // for(int i = 0; i < count; i++){
    //     for(int j = 0; j < count - i; j++){
    //         printf("%c", str[j]);
    //     }
    //     printf("\n");
    // }    
}