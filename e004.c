#include <stdio.h>
int main(void){
int i = 999;
int j, num, rem, rev, tmp;
int res = 0;
while (i > 99)
{
    j = i;
    while (j > 99)
    {
        num = i * j;
        tmp = num;
        rem = rev = 0;
        while (tmp > 0)
        {
            rem = tmp % 10;
            rev = rev * 10 + rem;
            tmp /= 10;
        }
        if (rev == num && res < num)
        {
            res = num;
        }
        j--;
    }
    i--;
}
printf("%d", res);
}

