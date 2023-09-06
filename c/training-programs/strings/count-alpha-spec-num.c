#include <stdio.h>
int main() {
   char str[256];
   int alpha=0, digit=0, specialChar = 0,count = 0, i;
   printf("Please Enter a String :  ");
   scanf("%[^\n]", str);
   for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
   for(i=0; i<count; i++)
   {
    if (str[i] >= 65 && str[i] <= 122)
      alpha++;
    else if (str[i] >= 48 && str[i] <= 57)
        digit++;  
    else
      specialChar++;
    }
   printf("alphabets = %d, digits = %d, specialChars = %d ", alpha, digit, specialChar);
   return 0;
}