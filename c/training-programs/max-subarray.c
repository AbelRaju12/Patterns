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

int maxSubArray(int arr[], int size) {
    int maxEndingHere = arr[0];
    int maxSoFar = arr[0];

    for (int i = 1; i < size; i++) {
        // Calculate the maximum sum ending at the current element
        maxEndingHere = (arr[i] > maxEndingHere + arr[i]) ? arr[i] : maxEndingHere + arr[i];

        // Update the maximum sum seen so far
        maxSoFar = (maxEndingHere > maxSoFar) ? maxEndingHere : maxSoFar;
    }

    return maxSoFar;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    readarray(arr, n);
    int maxSum = maxSubArray(arr, n);
    printf("Maximum subarray sum is %d\n", maxSum);
    return 0;
}