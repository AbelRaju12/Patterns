#include <stdio.h>
int main()
{
    char str1[256], str2[256],c;
    printf("Enter the first string : ");
    scanf("%[^\n]%c",str1,&c);
    printf("Enter the second string : ");
    scanf("%[^\n]%c",str2,&c);
    int temp = 0,i = 0;
    while(str1[i]!='\0' && str2[i]!='\0')
        {
        if(str1[i]!=str2[i])
        {
            temp=1;
            break;
        }
        i++;
        }
    if(temp==0)
        printf("strings are same");
    else
         printf("strings are not same");
    return 0;
}