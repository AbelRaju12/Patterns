#include <stdio.h>
#include <stdbool.h>
#include <limits.h>
#include <string.h>

// Function to Check if a substring is a palindrome
bool isPalindrome(char String[], int i, int j)
{
    while (i < j) {
        if (String[i] != String[j])
            return false;
        i++;
        j--;
    }
    return true;
}

// Function to find the minimum number of cuts needed for
// palindrome partitioning
int minPalPartion(char String[], int i, int j)
{
    // Base case: If the substring is empty or a palindrome,
    // no cuts needed
    if (i >= j || isPalindrome(String, i, j))
        return 0;

    int ans = INT_MAX, count;

    // Iterate through all possible partitions and find the
    // minimum cuts needed
    for (int k = i; k < j; k++) {
        count = minPalPartion(String, i, k)
                + minPalPartion(String, k + 1, j) + 1;
        ans = ans < count ? ans : count;
    }

    return ans;
}

// Driver code
int main()
{
    char str[100];
    scanf("%[^\n]", str);

    // Find the minimum cuts needed for palindrome
    // partitioning and display the result
    printf("Min cuts needed for Palindrome Partitioning is %d\n", minPalPartion(str, 0, strlen(str) - 1));

    return 0;
}