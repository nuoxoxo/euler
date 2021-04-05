#include <stdio.h>

int main(void)
{
   int start = 2520;
   int i = 11;
   int j, k;
   while (i < 21)
   {
        if (start % i != 0)
        {
            j = 2;
            k = 0;
            while (j < i + 1)
            {
                if (i % j == 0 && k < 1)
                {
                    start *= j;
                    k++;
                }
                j++;
            }
        }
        i++;
   }
   printf("%d", start);
}
