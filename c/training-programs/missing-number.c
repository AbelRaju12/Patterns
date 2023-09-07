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

void missingnum(int arr[], int n){
    int temp[n + 1], target;
    for(int i = 0; i < n; i++){
        temp[i] = 0;
    }
    for(int i = 0; i < n; i++){
        temp[arr[i] - 1] = 1;
    }
    for(int i = 0; i < n; i++){
        if(temp[i] == 0)
            target = i + 1;
    }
    printf("The missing number is %d", target);

}

int main(){
    printf("Enter the size of the array: ");
    int n;
    scanf("%d", &n);
    int arr[n];
    readarray(arr, n);
    missingnum(arr, n);
    return 0;
}