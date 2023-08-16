#include <stdio.h>
int sum = 0; // or declare static
int sumofdig(int num){
    // static int sum = 0;
    int rem;
    sum = sum + (num % 10);
    rem = num / 10;
    if(rem > 0){
        sumofdig(rem);
    }
    return sum;
}
int main() {
  int j, num;
  printf("Please enter a number :");
  scanf("%d", & num);
  printf("sum of digits of the number = %d ", sumofdig(num));
}