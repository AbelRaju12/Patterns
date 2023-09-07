#include <stdio.h>

void readarray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("Enter element no. %d -> ", i + 1);
        scanf("%d", &arr[i]);
    }
}

void printarray(int arr[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", arr[i]);
     }
}

void reverse(int arr[], int start, int end){
    while(start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotate(int arr[], int n, int k){
    k = k % n; // In case k is greater than the n of the array
    if (k < 0)
        k += n; // Handle negative k values

    reverse(arr, 0, n - 1);
    reverse(arr, 0, k - 1);
    reverse(arr, k, n - 1);

}

int main(){
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);
    int arr[n];
    readarray(arr, n);
    printf("Enter the number of steps to be rotated: ");
    int k;
    scanf("%d", &k);
    rotate(arr, n, k);
    printarray(arr, n);
    return 0;
}