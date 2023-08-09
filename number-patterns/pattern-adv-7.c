// 1
// 2 4
// 1 3 5
// 2 4 6 8
// 1 3 5 7 9
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        if ( i % 2 == 0){
            k = 2;
        }
        else{
            k = 1;
        }
        for(int j = 1; j <= i; j++){  
            printf("%d ",k);
            k += 2;
        }
        
        printf("\n");
    }
    return 0;
}