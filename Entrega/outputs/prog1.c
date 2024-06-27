#include <stdio.h>

int main() {
int X;
int Y;
int Z;
Y = 2;
X = 5;
Z = Y;
printf("'Z = Y;' => Z = %d\n", Z);
while (X != 0) {
Z = Z + 1;
printf("'Z = Z + 1;' => Z = %d\n", Z);
X = X + -1;
}

return 0;
}