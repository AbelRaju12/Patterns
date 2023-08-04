#include <stdio.h>

int main(){
    int num;
    char ch[100];
    scanf("%d", &num);
    for(int i = 0; i <= num; i++){
        for(int j = 0; j <= num; j++){
            if(j > i){
                printf("* ");
            }
        }
        printf("\n");
    }
    return 0;
}