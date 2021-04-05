#include <stdio.h>
#include <math.h>
int main(void){
int x = 0, y = 0, i = 0;
while (i <= 100)
{
    x += pow(i, 2);
    y += i;
    i++;
}

int df;
df = pow(y, 2) - x;
printf("%d, %d, %d", x, y, df);
}
