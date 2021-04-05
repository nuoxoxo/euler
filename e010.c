#include <stdio.h>
#include <math.h>

int main()
{
    long somme = 5;
    int a = 5;
    int z = 2000000;
    int i, count;
    while (a < z)
    {
        count = 0;
        i = 2;
        while (i < floor(sqrt(a)) + 1)
        {
            if (a % i == 0)
            {
                count++;
                break;
            }
            i++;
        }
        if (count == 0)
        {
            somme += a;
        }
        a += 2;
    }
    
    printf("%ld", somme);

    return (0);
}

