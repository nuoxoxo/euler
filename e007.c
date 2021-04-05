#include <stdio.h>

int isp(n)
{
    int i = 2;
    int c = 1;
    while (i <= n / 2)
    {
        if (n % i == 0)
        {
            c = 0;
            break;
        }
        i++;
    }
    return (c);
}

int main(void)
{
    int counter = 2;
    int start = 3;
    /// set counter to 2 and starting point to 3 because
    /// the (+2) pattern begins at 3
    /// before 3 there is 2 when counter == 1
    int goal = 10002;
    while (counter < goal)
    {
        if (isp(start) == 1)
        {
            counter++;
        }
        if (counter == goal)
        {
            printf("%d", start);
            break;
        }
        start += 2;
    }
}
