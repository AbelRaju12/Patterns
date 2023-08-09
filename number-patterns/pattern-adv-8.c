// 1 
// 1 3 1 
// 1 3 5 3 1 
// 1 3 5 7 5 3 1 
// 1 3 5 7 9 7 5 3 1 
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        k = 1; // k = 2
        for(int j = 1; j <= i; j++, k += 2){  // + = 1 and -= 1 for 121, 12321 etc.
            printf("%d ",k); 
        }
        k -= 2;
        for(int j = 2; j <= i; j++){
            k -= 2;
            printf("%d ", k);

        }
        
        printf("\n");
    }
    return 0;
}