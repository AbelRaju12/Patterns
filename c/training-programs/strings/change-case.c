#include<stdio.h>
int main()
{
    char str[100];
    int i = 0;
    printf("Convert lower case into upper case Char using C \n");
    printf("Please enter a string: ");
    fgets(str, 100, stdin);
    while( str[i] != '\0' )
    {
        if( str[i] >= 'a' && str[i] <= 'z' )
        {
            str[i] = str[i] - 32;
        }
        i++;
    }
    printf("String after converting into upper case : \n%s", str);
    return 0;
}


// int main()
// {
//     char str[100];
//     int i = 0;
//     printf("C Program to Convert lower case vowel to upper case of String  \n");
//     printf("Please enter a string: ");
//     fgets(str, 100, stdin);
//     while( str[i] != '\0' )
//     {
//         if(str[i]=='a' ||str[i]=='e' ||str[i]=='i' ||str[i]=='o' ||str[i]=='u')
//         {
//             str[i] = str[i] - 32;
//         }
//         i++;
//     }
//     printf("Vowel after converting into upper case = %s ", str);
//     return 0;
// }

// int main()
// {
//     char str[100];
//     int i,j,len=0;
//     printf("C program to delete all vowels from String \n");
//     printf("Please enter a string : ");
//     fgets(str, 100, stdin);
//     len=strlen(str);
//     for(i=0; i<len; i++)
//     {
//         if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
//         {
//             for(j=i; j<len; j++)
//             {
//                 str[j]=str[j+1];
//             }
//             i--;
//             len--;
//         }
//     }
//     printf("After deleting the vowels string is : %s",str);
//     return 0;
// }