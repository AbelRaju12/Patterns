#include <stdio.h>

void twoSum(int arr[], int size, int target) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (arr[i] + arr[j] == target) {
                printf("Indices: %d, %d\n", i, j);
                return;
            }
        }
    }
    printf("No such pair exists.\n");
}

int main() {
    int n, sum = 0, count = 0, max = 0;
    scanf("%d",&n);
    int arr[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }
    int target;
    scanf("%d", &target);
    int size = sizeof(arr) / sizeof(arr[0]);

    twoSum(arr, size, target);

    return 0;
}