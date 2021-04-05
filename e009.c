#include <stdio.h>
#include <math.h>

int main(void)
{
    int a = 1;
    int b, c, n;
    while (a < 1000)
    {
        b = a;
        while (b < 1000)
        {
            c = 1000 - a - b;
            if (pow(c, 2) == pow(a, 2) + pow(b, 2))
            {
                n = a * b * c;
                break;
            }
            b++;
        }
        a++;
    }
    printf("%i", n);
}
