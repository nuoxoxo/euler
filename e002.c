#include <stdio.h>
#include <math.h>

int main(void)
{
    int a, b, c, somme, max;
    a = b = c = 1;
    somme = 0;
    max = 4 * pow(10, 6);
    while (c <= max)
    {
        if (c % 2 == 0)
        {
            somme += c;
        }
        c = a + b;
        a = b;
        b = c;
    }

    printf("%i", somme);

}
