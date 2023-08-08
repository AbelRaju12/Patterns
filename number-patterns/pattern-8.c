//1
//23
//345
//4567
//567
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1, k = i; j <= i; j++, k++){
            printf("%d ", k);         
        }
        printf("\n");
    }
    // for(int i = 1; i <= num; i++){
    //     for(int j = 1; j <= i; j++, k++){
    //         printf("%d ", k);         
    //     }
    //     printf("\n");
    //  }
    return 0;
}