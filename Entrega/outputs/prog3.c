#include <stdio.h>

int main() {
int X;
int Y;
int L;
int Z;
Z = 0;
printf("'Z = 0;' => Z = %d\n", Z);
Z = 2;
printf("'Z = 2;' => Z = %d\n", Z);
X = 5;
Y = 0;
L = 1;
if (Y) {
for (int i = X; i > L; --i) {
Z = Z * L;
printf("'Z = Z * L;' => Z = %d\n", Z);
}
} else {
for (int i = X; i > L; --i) {
Z = Z * X;
printf("'Z = Z * X;' => Z = %d\n", Z);
}
}

return 0;
}