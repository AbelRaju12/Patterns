#include<stdio.h>
#include<stdlib.h>
int main(){
    int n, flag = 0;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 1; j < n; j++){
            if(i == j){
                continue;
            }
            if(arr[i] == arr[j]){
                printf("%d repeats first", arr[i]);
                exit(0);
            }
        }
    }
    return 0;
}