#include <stdio.h>
void readarray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("Enter element no. %d ->", i + 1);
        scanf("%d", &arr[i]);
    }
}

void printarray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
     }
}

void twosum(int arr[], int n, int target){
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            if(arr[i] + arr[j] == target){
                printf("%d and %d elements in the array gives the sum of %d", i+1, j+1, target);
            }
        }
    }
}

int main(){
    printf("Enter the size of the array: ");
    int n, target;
    scanf("%d", &n);
    int arr[n];
    readarray(arr, n);
    printf("Enter the target value required -> ");
    scanf("%d", &target);
    twosum(arr, n, target);
    return 0;
}