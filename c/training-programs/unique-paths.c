#include <stdio.h>
int uniquePaths(int rows, int coloumns){
    int dp[rows][coloumns];
    
    for(int i = 0; i < rows; i++){
        dp[i][0] = 1;
    }
    for(int i = 0; i < coloumns; i++){
        dp[0][i] = 1;
    }

    for(int i = 1; i < rows; i++){
        for(int j = 1; j < coloumns; j++){
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    return dp[rows - 1][coloumns - 1];
}

int main(){
    int rows = 3, coloumns = 7;
    
    int paths = uniquePaths(rows, coloumns);
    
    printf("Number of Unique Paths: %d\n", paths);

    return 0;
}