// 2520 is the smallest number that can be divided by each 
// of the numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible 
// by all of the numbers from 1 to 20?

class Master
{
    public static void main(String[] args)
    {
        int num = 2520;
        int div, i, j;
        for (div = 11; div < 21; div++)
        {
            if (num % div != 0)
            {
                i = 2;
                j = 0;
                while (div + 1 > i)
                {
                    if (div % i == 0 && j < 1)
                    {
                        num *= i;
                        j++;
                    }
                    i++;
                }
            }
        }
        System.out.print(num);
    }
    
}
