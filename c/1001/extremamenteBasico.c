/**
 * Author: Weder Carlos
 * Date: 01/05/2022
 * To compile: gcc <file_name>.c -o <name_to_execute>
 * To run: ./<name_to_execute>.out
*/

#include <stdio.h>

int main() {
    int A, B, X;
    scanf("%d", &A);
    scanf("%d", &B);
    X = A + B;
    printf("X = %d\n", X);

    return 0;
}