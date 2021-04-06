public class Demo
{
    public static boolean isPalin(int n)
    {
        int tmp, rem, rev;
        
        tmp = n;
        
        rem = 0;
        rev = 0;

        while (tmp > 0)
        {
            rem = (int) tmp % 10;
            rev = 10 * rev + rem;
            
            tmp /= 10;
        }

        if (rev == n)
            return true;

        return false;
    }

    public static void main(String args[])
    {
        int target, product, x, y;
        target = 0;
        x = 999;

        while (x > 99)
        {
            y = x;

            while (y > 99)
            {
                product = x * y;

                if (isPalin(product) == true && product > target)
                {
                    target = product;
                    break;
                }
                y--;
            }
            x--;
        }

        System.out.println(target);
    }
}

