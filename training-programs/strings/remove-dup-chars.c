#include <stdio.h>
int main()
{
    char str[256],c;
    int count = 0;
    printf("Enter the string : ");
    scanf("%[^\n]%c",str,&c);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++){
        for(int j = i + 1; j < count;j++){
            if(str[i] == str[j]){
                for(int k = j; k < count; k++){
                    str[k] = str[k+1];
                }
                count--;
                j--;
            }
        }
    }
    printf("String after removing duplicate values = %s",str);
    return 0;
}