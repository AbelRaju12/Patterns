#include<stdio.h>
#include<stdbool.h>
int max(int i, int j){
    return (i > j) ? i : j;
}
bool areDistinct(char string[], int i, int j){
    bool visited[256];
    for(int i = 0;i < 256; i++){
        visited[i] = 0;
    }
    for(int k = i; k <= j; k++){
        if(visited[string[k]] == true){
            return false;
        }
        visited[string[k]] = true;
    }
    return true;
}
int uniquesubstring(char string[]){
    int n = 0, res = 0;
    char ch[256];
    for(int i = 0; string[i]; i++){
        n++;
    }
    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            if(areDistinct(string, i, j)){
                res = max(res, j - i + 1);
            }
        }
    }
    return res;    
}
void main(){
    char string[100];
    printf("Enter the string: ");
    gets(string);
    int len = uniquesubstring(string);
    printf("%d", len);
}