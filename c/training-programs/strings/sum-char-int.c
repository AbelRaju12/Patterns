#include <stdio.h>
int main() {
   char str[256];
   int count = 0, i, sum = 0;
   printf("Please Enter a String :  ");
   scanf("%[^\n]", str);
   for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
   for(i = 0; i < count; i++){
    if (str[i] >= 48 && str[i] <= 57){
        sum = sum + (str[i] - '0');
        }
    }
    printf("Sum of digits inside string is = %d",sum);
    return 0;
}