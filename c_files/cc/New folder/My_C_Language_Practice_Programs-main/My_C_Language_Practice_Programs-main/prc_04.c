// Q1. Write a c program to calculate the area of a rectangle:
// a) using hardcoded inputs & 
// b) using inputs supplied by the user
//              (b)
#include<stdio.h>
int main(){
    int length, breadth;
    printf("What is the length of the rectangle\n");
    scanf("%d", &length);

    printf("What is the breadth of the rectangle\n");
    scanf("%d", &breadth);

    printf("The area of your rectangle is %d", length*breadth);
    return 0;
}