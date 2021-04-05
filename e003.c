#include <stdio.h>
#include <math.h>

//int main(void)
int e3(long num)
{
    //long num = 600851475143;
    int i = floor(sqrt(num / 2));
    int j = 0;
    if (i % 2 == 0)
    {
        i -= 1;
    }

    int mxp = 0;

    while (i > 0)
    {
        j = 2;
        if (num % i == 0)
        {
            //printf("%d\n", i);
            int counter = 0;
            while (j <= i / 2)
            {
                if (i % j == 0)
                {
                    counter++;
                }
                j++;
            
            }
            if (counter == 0)
            {
                mxp = i;
                break;
            }
        }
        i -= 2;
    }
    printf("%d\n", mxp);
    return (0);
}



// driver

int main(void)
{
    int n = 13195;
    e3(n);
    
    long num = 600851475143;
    e3(num);

    return (0);

}


