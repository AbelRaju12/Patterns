#include <stdio.h>
int main(){
    int a[100], n, sum = 0, count = 0, max = 0;
    scanf("%d",&n);
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for(int i = 0; i < n; i++){
        if(a[i] >= 0){
            sum = sum + a[i];
            count++;
        }
        else{
            if(a[i] > max){
                max = a[i]; // if its just negative numbers then we need to print the largest neative number
                if(a[i] == 0){
                    count++;
                }
            }
            
        }
    }
    if(sum == 0 && max < 0){
        count ++;
        }
    printf("%d %d",sum,count);
    return 0;
}