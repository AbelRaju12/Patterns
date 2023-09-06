//        t
//       o m
//      a t o
//     t o m a
//    t o t o m
//   a t o t o m

#include <stdio.h>
#include <stdlib.h>
int main(){
    char str[20];
    int count = 0, a = 0;
    printf("Enter a string: ");
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++){
        for(int j = 0; j < count - i; j++){
            printf(" ");
        }
        for(int j = 0; j <= i; j++){
            printf("%2c", str[a++]);
            if(str[a]== '\0'){
                a=0;
            }
        }
        printf("\n");
    }
    // a = 0;
    // for(int i = 0; i < count; i++){
    //     for(int j = 0; j <= i + 1; j++){  // trial and error
    //         printf(" ");
    //     }
    //     for(int j = i + 1; j < count; j++){
    //         printf("%2c", str[a++]);
    //         if(str[a]== '\0'){
    //             a=0;
    //         }
    //     }
    //     printf("\n");
    // }
    return 0;
}