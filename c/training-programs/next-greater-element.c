#include <stdio.h>
void nextgreat(int a[], int n){
    for(int i = 0; i < n; i++){
        int next = -1;
        for(int j = i; j < n; j++){
            if(a[j] > a[i]){
                next = a[j];
                break;
            }
        }
        printf("%d ----> %d\n", a[i], next);
    }
}
int main(){
    int n;
    scanf("%d", &n);
    int a[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    nextgreat(a, n);
    return 0;
}