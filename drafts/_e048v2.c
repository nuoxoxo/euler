#include <stdio.h>
#include <math.h>

// Solution below is invalid
// Reason: 
// number got very big at around 15th step
// no viable way to deal with big int 

int main(void)
{
    long long some = 0;
    int i = 1;
    while (i < 1001)
    {
        some += pow(i, i);
        some %= (int) round(pow(10, 10));
        i++;
        printf("%lld\n", some);
    }
    
    printf("%lld\n", some);
/*
    int arr[10];
    i = 1;
    while (i < 11)
    {
        arr[10 - i] = some % 10;
        some /= 10;
        i++;
    }
    i = 0;
    while (i < 10)
    {
        printf("%i\n", arr[i]);
        i++;
    }

*/
}
